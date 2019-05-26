import numpy as np
import csv
from pyspark import SparkConf, SparkContext
conf = SparkConf()
conf.set("spark.master","yarn")
conf.set("spark.app.name","My app")
sc = SparkContext(conf=conf)

x = []
y = []

data = sc.textFile("file:///home/swe3033/local/data/letter-recognition.csv")
data1 = sc.textFile("file:///home/swe3033/local/data/letter-recognition.csv") 



 
num =0
def get(line):	
	global num
	num = num +1
	cnt = line.split(',')
	label = cnt[0]
	feature = []
	for i in range(1,17):
		feature.append(int(cnt[i]))

	return label,feature,num

test_data = data.map(get).collect()


#test_data = test_data.collect()


tlist = [0,1289,2578,3867]
def KNN(truth,feature,num):
	for i in range(3):
		snum = tlist[i]
		enum = tlist[i+1]
		if num >snum and num <=enum:
			check = [[10000000,0],[10000000,0],[10000000,0]]
			for train in test_data:
				if train[2] <=snum or train[2] >enum:
					temp = 0
					for i in range(len(train[1])):
						temp += pow(feature[i] - train[1][i],2)
					temp = np.sqrt(temp)
					z = [temp,train[0]]
					for w in range(0,3):
						if check[w][0] > temp:
							check.insert(w,z)
							break
			if check[1][1] == check[2][1]:
				return check[1][1]
			else:
				return check[0][1]
test = data1.map(get)		
pred = test.map(lambda (truth,feature,num) : KNN(truth,feature,num)).collect()
'''

f = open('./home/2013314264/result.csv','w')
wr = csv.writer(f)
for i in pred:
	wr.writerow(i)

f.close()
'''
