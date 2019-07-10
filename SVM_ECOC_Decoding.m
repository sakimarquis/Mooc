% This function does EEG decoding.

function SVM_ECOC_Decoding(subs)

delete(gcp) % delete current parallel pool
parpool % create parallel pool

% set subjects' numbers
if nargin == 0
    subs = [505 506 507 508 509 510 512 514 516 517 519 520 521 523 524 525];
end
nSubs = length(subs);

% parameters to set
% svmECOC is a struct to save the parameter and results
svmECOC.nChans = 16; % # of channels
svmECOC.nBins = svmECOC.nChans; % # of stimulus bins
svmECOC.nIter = 10; % # of iterations
svmECOC.nBlocks = 3; % # of blocks for cross-validation
svmECOC.frequencies = [0 6]; % low pass filter, freqs to filter
svmECOC.time = -500:20:1496; % time points of interest in the analysis
svmECOC.window = 4; % 1 data point per 4 ms in the preprocessed data
svmECOC.srate = 250; % samplring rate of in the preprocessed data for filtering
ReleventChan = sort([2,3,4,18,19, 5,6,20, 7,8,21, 9,10,11,12,13,14, 22,23,24,25,26,27, 15,16,1,17]); %electrodes
svmECOC.nElectrodes = length(ReleventChan); % # of electrode included in the analysis

% for brevity in analysis
nChans = svmECOC.nChans;
nBins = svmECOC.nBins;
nIter = svmECOC.nIter;
nBlocks = svmECOC.nBlocks;
freqs = svmECOC.frequencies;
times = svmECOC.time;
nElectrodes = svmECOC.nElectrodes;
nSamps = length(svmECOC.time);
srate = svmECOC.srate;

%% Loop through condition
for cond = 1:1
    % 1: orientation
    
%% Loop through participants
for subs_idx = 1:nSubs
    
    sub = subs(subs_idx);
    fprintf('Subject:\t%d\n',sub)

    % load data
    currentSub = num2str(sub);
    dataLocation = pwd; % set directory of data set
    loadThis = strcat(dataLocation,'/Decoding_DE_',currentSub,'.mat'); % choose filename
    load(loadThis)
    
    % where to save decoding output
    saveLocation = pwd; % set directory for decoding results.
    
    % set up location bin of each trial
    channel = data.channel; % tip location of sample teardrop 
    svmECOC.posBin = channel'; % add to fm structure so it's saved
    posBin = svmECOC.posBin;
    
    % grab EEG data
    eegs = data.eeg(:,ReleventChan,:); 
   
    % set up time points
    tois = ismember(data.time.pre: 4: data.time.post,svmECOC.time); 
    nTimes = length(tois);
    
    % # of trials
    svmECOC.nTrials = length(posBin); 
    nTrials = svmECOC.nTrials; 

    % Preallocate Matrices
    svm_predict = nan(nIter,nSamps,nBlocks,nChans); % a matrix to save prediction from SVM
    test_target = nan(nIter,nSamps,nBlocks,nChans);  % a matrix to save true target values
    svmECOC.blocks = nan(nTrials,nIter);  % create svmECOC.block to save block assignments

    % low-pass filtering
    filtData = nan(nTrials, nElectrodes, nTimes); % Preallocate Matrices
    low_cutoff = freqs(1);
    high_cutoff = freqs(2);
    parfor electrodes_idx = 1:nElectrodes
        % ERP low pass filter
        filtData(:,electrodes_idx,:) = eegfilt(squeeze(eegs(:,electrodes_idx,:)), srate, low_cutoff, high_cutoff);
        % Instantaneous frequency power analysis
        %filtData(:,electrodes_idx,:) = abs(hilbert(eegfilt(squeeze(eegs(:,c,:)), srate,low_cutoff, high_cutoff)')').^2;
    end

    % Loop through each iteration
    % To minimize idiosyncrasies associated with the assignment of trials to groups, 
    % we iterated the entire procedure 10 times with new random assignments of trials to the three groups
    tic % start timing iteration loop

    for iter = 1:nIter % 10
        % preallocate arrays
        blocks = nan(size(posBin)); % 640
        shuffle_blocks = nan(size(posBin));
        
        % count number of trials within each position bin
        clear bin_count
        for bin = 1:nBins  % 16, iterate through the location
            bin_count(bin) = sum(posBin == bin); % 40 trials * 16 locations matrix
        end
        min_count = min(bin_count); % 40, # of trials for position bin with fewest trials
        max_trials = floor(min_count/nBlocks); % 13, max # of trials such that the # of trials for each bin can be equated within each block

        % shuffle trials
        shuffle_idx = randperm(nTrials)'; % create shuffle index
        shuffled_trials = posBin(shuffle_idx); % shuffle trial order

        % take first max_trials ¡Á number of trials for each position bin.
        for bin = 1:nBins;  % 16 
            idx = find(shuffled_trials == bin); % 40 get index for trials belonging to the current bin
            idx = idx(1:max_trials*nBlocks); % 39 drop excess trials
            x = repmat((1:nBlocks)',max_trials,1); % 39 [123123.....123]'
            % assign randomly order trials to blocks
            shuffle_blocks(idx) = x; % 640 ¡Á 1, 208 times 1&2&3, 16 times nan  
        end

        % unshuffle block assignment
        blocks(shuffle_idx) = shuffle_blocks;

        % save block assignment
        svmECOC.blocks(:,iter) = blocks; % 640 ¡Á 10 nan, block assignment
        svmECOC.nTrialsPerBlock = length(blocks(blocks == 1)); % 208, # of trials per block

        % Average data for each stimulus position bin across blocks
        averaged_data = nan(nBins*nBlocks,nElectrodes,nSamps);  % averaged & filtered EEG data with resampling at 50 Hz
        labels = nan(nBins*nBlocks,1);                          % bin labels for averaged & filtered EEG data
        blockNum = nan(nBins*nBlocks,1);                        % block numbers for averaged & filtered EEG data
        cnt = 1;

        for bin_idx = 1:nBins
            for block_idx = 1:nBlocks
                % average the 13 trails, [1¡Á27¡Á100] iterate 48 times
                averaged_data(cnt,:,:) = squeeze(mean(filtData(posBin==bin_idx & blocks==block_idx, :, tois),1)); 
                labels(cnt) = bin_idx;
                blockNum(cnt) = block_idx;
                cnt = cnt+1;
            end
        end

        % Do SVM_ECOC at each time point
        parfor time_idx = 1:nSamps
            % grab data for timepoint time_idx
            toi = ismember(times, times(time_idx) - svmECOC.window/2: times(time_idx) + svmECOC.window/2);

            % average across time window of interest
            dataAtTimeT = squeeze(mean(averaged_data(:,:,toi),3));  
            
            % Do SVM_ECOC for each block
            for i = 1:nBlocks % loop through blocks, holding each out as the test set
                train_label = labels(blockNum ~= i); % 32 ¡Á 1
                test_label = labels(blockNum == i);  % 16 ¡Á 1
                train_data = dataAtTimeT(blockNum ~= i,:); % 32 ¡Á 27
                test_data = dataAtTimeT(blockNum == i,:);  % 16 ¡Á 27

                % SVM_ECOC
                classifier = fitcecoc(train_data, train_label, 'Coding','onevsall','Learners','SVM' ); % train support vector machine
                label_predicted = predict(classifier, test_data);     % predict classes for new data
                svm_predict(iter, time_idx, i, :) = label_predicted;  % save predicted labels
                test_target(iter, time_idx, i, :) = test_label;       % save true target labels

            end % end of block
        end % end of time points
    end % end of iteration
    toc % stop timing the iteration loop

    % save the results in variable svmECOC
    OutputfName = strcat(saveLocation,'/Orientation_Results_ERPbased_',currentSub,'.mat');
    svmECOC.targets = test_target;
    svmECOC.modelPredict = svm_predict; 
    svmECOC.nBlocks = nBlocks;
    save(OutputfName,'svmECOC','-v7.3');

end % end of subject loop
end % end of condition loop
