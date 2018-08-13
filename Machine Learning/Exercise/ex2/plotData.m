function plotData(X, y)
%PLOTDATA Plots the data points X and y into a new figure 
%   PLOTDATA(x,y) plots the data points with + for the positive examples
%   and o for the negative examples. X is assumed to be a Mx2 matrix.

% Create New Figure
figure; hold on;

% ====================== YOUR CODE HERE ======================
% Instructions: Plot the positive and negative examples on a
%               2D plot, using the option 'k+' for the positive
%               examples and 'ko' for the negative examples.
%

%索引出两个不同的类别
plot(X(find(y==1), 1), X(find(y==1), 2), 'r+','markersize', 7);
plot(X(find(y==0), 1), X(find(y==0), 2), 'co','markersize', 7);

% =========================================================================



hold off;

end
