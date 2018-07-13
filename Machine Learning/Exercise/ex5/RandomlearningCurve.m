function [error_train, error_val] = ...
    RandomlearningCurve(X, y, Xval, yval, lambda, iter)

m = size(X, 1);

error_train_set = zeros(m, iter);
error_val_set   = zeros(m, iter);

for i = 1:m;
    for j = 1:iter;
        sel = randperm(m)'(1:i,:);
        theta = trainLinearReg(X([sel],:), y(sel), lambda);
        error_train_set(i,j) = sum((X([sel],:) * theta - y(sel)).^2)/(2*i);
        error_val_set(i,j)   = sum((Xval([sel],:)  * theta - yval(sel)).^2)/(2*i);
    end
end

error_train = mean(error_train_set')';
error_val  = mean(error_val_set')';
