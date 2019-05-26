% original data: https://archive.ics.uci.edu/ml/datasets/Energy+efficiency
clear
format longG
load hw1_data.txt
X=hw1_data(:,1:8);
Y=hw1_data(:,9:10);
y=Y(1:end,1);
X=X(1:end,1:2);
save('hw1_data1.mat','X','y');

clear
load hw1_data1.mat
X_train = X(1:400,1:2);
X_train = [ones(400,1),X_train]
X_test = X(401:end,1:2);
X_test = [ones(368,1),X_test]
y_train = y(1:400,1);
y_test = y(401:end,1);

%least square

phi = round((inv(X_train'*X_train))*X_train'*y_train,4);
cnt = X_test*phi;
plot(X_test(:,3),cnt(1:368),'*',X_test(:,3),y_test(1:368),'*');
legend('least square','ground truth')
xlabel('Surface area')
ylabel('Heating label')
RMSE = round(sqrt(mean((y_test-cnt).^2)),8)