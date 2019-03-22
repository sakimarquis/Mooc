%% 4.7.1 Exercises for Script A
% 1.Create a 4 ¡Á 8 matrix of randomly generated numbers.

ans1 = rand(4,8);

% 2.Loop through all rows and columns, and test whether each element is 
%   greater than 0.5.

ans2 = ans1 < 0.5;

% 3.Report the results of the test along with the value of the matrix 
%   element and its row-column position. For example, your Matlab script 
%   should print "The 3rd row and 8th column has a value of 0.42345 and is 
%   not bigger than 0.5".

% 4.Make sure to add exceptions to print out 1st, 2nd, and 3rd, instead of 
%   1th, 2th, and 3th.

for i = 1:size(ans1,1)
    for j = 1:size(ans1,2)
        if ans1(i,j) < 0.5
            switch i
                case 1
                    row_excep = 'st';
                case 2
                    row_excep = 'nd';
                case 3
                    row_excep = 'rd';
                otherwise
                    row_excep = 'th';
            end
            switch j
                case 1
                    column_excep = 'st';
                case 2
                    column_excep = 'nd';
                case 3
                    column_excep = 'rd';
                otherwise
                    column_excep = 'th';
            end
            disp(['The ' num2str(i) row_excep ' row and ' num2str(j) column_excep ' column has a value of ' num2str(ans1(i,j)) ' and is not bigger than 0.5.'])
        end
    end
end

% 5.Put this code into a separate function that you can call from the 
%   command line with two inputs, corresponding to the number of rows and 
%   the number of columns of the matrix.

rows = 5;
columns = 5;
chapter04_ex5_func(rows,columns)

%% 4.7.2 Exercises for Script B

% 6.Import and plot the picture of Amsterdam that comes with the online 
%   Matlab code.

amsterdam = imread('amsterdam.bmp');

figure
imagesc(amsterdam)

% 7.On top of the picture, plot a thick red line from¡° Nieuwmarkt ¡± (near 
%   the center of the picture) to ¡° Station Amsterdam Centraal ¡± (near the 
%   top of the picture).

hold on
plot([380 395],[330 75],'r','LineWidth',2)

% 8.Plot a magenta star over the Waterlooplein metro station (a bit South 
%   of Nieuwmarkt).

plot(375,500,'*m')
hold off

% 9.Find the maximum value on each color dimension (red, green, or blue) 
%   and plot a circle using that color. There may be more than one pixel 
%   with a maximum value; if so, pick one pixel at random.

max_r = max(max(amsterdam(:,:,1)))
max_g = max(max(amsterdam(:,:,2)))
max_b = max(max(amsterdam(:,:,3)))

t = 0: pi/100: 2*pi;
x = sin(t);
y = cos(t);
plot(x,y,'Color',[max_r,max_g,max_b])
axis equal
colordef black

colordef none

%%  4.7.3 Exercises for Script C

% 10.From the function you wrote for exercise 5, generate a 32 ¡Á 3 number matrix 
%    in which the three numbers in each row correspond to the row, column, and 
%    result of the test (1 for bigger than 0.5; 0 for smaller than 0.5).

ex10_mat = chapter04_ex5_func(32,3);

% 11.Write this 32 ¡Á 3 matrix to a text file that contains this matrix along 
%    with appropriate variable labels in the first row. Make sure this file 
%    is tab-delimited and readable by a spreadsheet software such as Microsoft 
%    Excel or Open Office Calc.

file = fopen('chapter04_ex11_data.txt','w');

% to txt file
variable_labels = {'var1';'var2';'var3'};

for vari = 1:length(variable_labels)
    fprintf(file,'%s\t',variable_labels{vari});
    % the %s is for string; %g is for number.
end

% insert a new-line character
fprintf(file,'\n');

for rowi = 1:size(ex10_mat,1)
    
    % now loop through columns (variables)
    for columni = 1:size(ex10_mat,2)
        fprintf(file,'%g\t',ex10_mat(rowi,columni));
    end
    fprintf(file,'\n'); % end-of-line 
    
    % You could also do this in one line:
    % fprintf(fid,'%s\t%g\t%g\t%g\t%g\n',subject_names{datarowi},behavioral_data(datarowi,1),behavioral_data(datarowi,2),behavioral_data(datarowi,3),behavioral_data(datarowi,4));
    
    fprintf('Finished writing line %g of %g\n',rowi,size(ex10_mat,1));
end

fclose(file);

% to csv file
xlswrite('chapter04_ex11_data.csv', {'var1','var2','var3'})
xlswrite('chapter04_ex11_data.csv', double(ex10_mat), 'A2:C33')
