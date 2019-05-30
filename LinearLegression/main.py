import csv
import numpy as np

class LinearRegression():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.num_data = self.x.shape[0]
        self.num_feature = self.x.shape[1]
        self.w = np.zeros(self.num_feature)

    def predict(self, x):


        return np.dot(x,self.w)

    def train(self, lr, epoch):
        for i in range(0, epoch):
            diff = np.dot(self.x, self.w) - self.y
            cost = np.sum(diff ** 2) / (2 * self.num_data)
            gradient = np.dot(np.transpose(self.x), diff) / self.num_data
            self.w = self.w - lr * gradient
            return self.w

def data_load(dana_name, tr_te):
    y = []
    x = []

    if dana_name == 'BloodPressure':
        if(tr_te == 'train'):
            file = './data/bloodPressure/train.csv'
        elif(tr_te == 'test'):
            file = './data/bloodPressure/test.csv'

        with open(file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                x.append([1, float(row[0])])
                y.append(float(row[1]))

    if dana_name == 'House':
        if(tr_te == 'train'):
            file = './data/house/train.csv'
        elif(tr_te == 'test'):
            file = './data/house/test.csv'

        with open(file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                x.append([1, float(row[1]), float(row[2]), float(row[3]), float(row[4])])
                y.append(float(row[0]))
    return np.array(x), np.array(y)

def eval(prediction, y):
    inner = np.power((prediction - y), 2)
    return np.sqrt(np.sum(inner) / len(y))

def main():
    X_train, Y_train = data_load('BloodPressure', 'train')
    model = LinearRegression(X_train, Y_train)
    model.train(0.00000001, 100) # learning rate, epoch

    X_test, Y_test = data_load('BloodPressure', 'test')
    prediction = model.predict(X_test)

    rmse = eval(prediction, Y_test)
    print("%.2f"%(rmse))


    X_train, Y_train = data_load('House', 'train')
    model = LinearRegression(X_train, Y_train)
    model.train(0.00000001, 100) # learning rate, epoch

    X_test, Y_test = data_load('House', 'test')
    prediction = model.predict(X_test)

    rmse = eval(prediction, Y_test)
    print("%.2f"%(rmse))
if __name__ == "__main__":
    main()


