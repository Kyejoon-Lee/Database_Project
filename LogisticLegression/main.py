import csv
import numpy as np

class LogisticRegression():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.num_data = self.x.shape[0]
        self.num_feature = self.x.shape[1]
        self.w = np.zeros(self.num_feature)

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def predict(self, x):

        predic = 1 / (1 + np.exp(-(np.dot(x, self.w))))

        index = np.where(predic > 0.5)[0]
        result = np.zeros(predic.shape)
        result[index] = 1
        return result

    def train(self, lr, epoch):
        for i in range(0, epoch):

            h = 1 / (1 + np.exp(-(np.dot(self.x,self.w))))
            ##cost = sum(self.y*np.log(h) + (1 - self.y)*np.log(1-h))//
            grad = np.dot(self.y - h, self.x)
            self.w = self.w + lr * grad
        return self.w


def data_load(dana_name, tr_te):
    y = []
    x = []

    if dana_name == 'Titanic':
        if(tr_te == 'train'):
            file = './data/titanic/train.csv'
        elif(tr_te == 'test'):
            file = './data/titanic/test.csv'

        with open(file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                y.append(float(row[0]))
                feature = [1] # bias
                feature.append(float(row[1])) # Pclass
                if(row[3] == 'male'):  # Sex
                    feature.append(float(0))
                else:
                    feature.append(float(1))
                feature.append(float(row[4]))  # Age
                feature.append(float(row[5]))  # Siblings/Spouses Aboard
                feature.append(float(row[6]))  # Parents/Children Aboard
                feature.append(float(row[7]))  # Fare
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
                    y.append(float(0))
                else:
                    y.append(float(1))

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
    model = LogisticRegression(X_train, Y_train)
    model.train(0.0001, 100) # learning rate, epoch

    X_test, Y_test = data_load('Iris', 'test')
    prediction = model.predict(X_test)

    accuracy = eval(prediction, Y_test)
    print("%.2f" % (accuracy))


    X_train, Y_train = data_load('Titanic', 'train')
    model = LogisticRegression(X_train, Y_train)
    model.train(0.001, 10000) # learning rate, epoch

    X_test, Y_test = data_load('Titanic', 'test')
    prediction = model.predict(X_test)

    accuracy = eval(prediction, Y_test)
    print("%.2f" % (accuracy))

if __name__ == "__main__":
    main()


