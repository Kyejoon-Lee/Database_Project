import csv
import numpy as np

class SoftmaxRegression():
    def __init__(self, x, y, num_label):
        self.x = x
        onehot = np.zeros((len(y), num_label))
        onehot[np.arange(len(y)), y] = 1
        self.y = onehot
        self.num_data = self.x.shape[0]
        self.num_feature = self.x.shape[1]

        self.num_label = num_label
        self.w = np.zeros((self.num_feature,self.num_label))

    def _softmax(self, z):

        e_z = np.exp(z-np.max(z))
        return e_z/e_z.sum()

    def predict(self, x):
        probs = self._softmax(np.dot(x, self.w))
        preds = np.argmax(probs, axis=1)
        return preds

    def train(self, lr, epoch):
        for i in range(0, epoch):
            h = self._softmax(np.dot(self.x,self.w))
            grad = np.dot(np.transpose(self.x), self.y - h)
            self.w = self.w + lr*grad

        return self.w


def data_load(dana_name, tr_te):
    y = []
    x = []

    if dana_name == 'Digit':
        if(tr_te == 'train'):
            file = './data/digit/train.csv'
        elif(tr_te == 'test'):
            file = './data/digit/test.csv'

        with open(file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                y.append(int(row[0]))
                feature = [1] # bias
                feature += list(map(int, row[1:785])) # pixel
                x.append(feature)

    if dana_name == 'Iris':
        if(tr_te == 'train'):
            file = './data/iris/train.csv'
        elif(tr_te == 'test'):
            file = './data/iris/test.csv'

        with open(file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                if (row[4] == 'Iris-setosa'):
                    y.append(int(0))
                elif(row[4] == 'Iris-versicolor'):
                    y.append(int(1))
                else:
                    y.append(int(2))

                feature = [1] # bias
                feature.append(float(row[0])) # sepal length in cm
                feature.append(float(row[1]))  # sepal width in cm
                feature.append(float(row[2]))  # petal length in cm
                feature.append(float(row[3]))  # petal width in cm
                x.append(feature)

    return np.array(x), np.array(y)


def eval(prediction, y):
    hit = 0
    for i, p in enumerate(prediction):
        if p == y[i]:
            hit += 1
    return hit/len(y)


def main():
    X_train, Y_train = data_load('Iris', 'train')
    model = SoftmaxRegression(X_train, Y_train, 3) # variables, label, # of class
    model.train(0.000001, 10000) # learning rate, epoch

    X_test, Y_test = data_load('Iris', 'test')
    prediction = model.predict(X_test)

    accuracy = eval(prediction, Y_test)
    print("%.2f" % (accuracy))


    X_train, Y_train = data_load('Digit', 'train')
    model = SoftmaxRegression(X_train, Y_train, 10) # variables, label, # of class
    model.train(0.001, 100) # learning rate, epoch

    X_test, Y_test = data_load('Digit', 'test')
    prediction = model.predict(X_test)

    accuracy = eval(prediction, Y_test)
    print("%.2f" % (accuracy))

if __name__ == "__main__":
    main()


