% original data: https://archive.ics.uci.edu/ml/datasets/Energy+efficiency
clear
format longG
load hw1_data.txt
X=hw1_data(:,1:8);
Y=hw1_data(:,9:10);
y=Y(1:end,1);
X=X(1:end,1:4);
save('hw1_data2.mat','X','y');

clear
load hw1_data2.mat

X_train = X(1:400,1:4);
X_train = [ones(400,1),X_train]
X_test = X(401:end,1:4);
X_test = [ones(368,1),X_test]
Y_train = y(1:400,1);
Y_test = y(401:end,1);

%least square

phi = round((inv(X_train' * X_train))*X_train'*Y_train,2)

least_cnt = X_test*phi;

%ridge regression

w = (inv(X_train' *X_train + 0.01))*X_train'*Y_train; 
w = round(w,4)

cnt = X_test*w;
plot(X_test(:,5),cnt,'*',X_test(:,5),Y_test,'*',X_test(:,5),least_cnt,'*');
legend('ridge','ground truth','least square');
xlabel('Roof area');
ylabel('Heating label');
Ridge_RMSE = round(sqrt(mean((Y_test-cnt).^2)),4)
Least_RMSE = round(sqrt(mean((Y_test-least_cnt).^2)),4)