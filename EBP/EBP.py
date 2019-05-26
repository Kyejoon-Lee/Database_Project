import numpy as np
import csv
x =[]
y =[]
for i in range(101):
    j = int(i)*0.01
    j = float("{0:.2f}".format(j))
    x.append(j)
    res = 4*j *(1-j)
    res = float("{0:.6f}".format(res))
    y.append(res)

weight1 = [0,0.5,-0.5,0]
weight2 = [0,0.75,-0.75,0]
result1 = []
def iteration(itr):
    global weight1
    global weight2
    global result1
    for i in range(itr):
        E = []
        for j in range(101):
            net = []
            h = []
            O=0
            temp1 = []
            for k in range(4):
                temp = weight1[k] * x[j]
                net.append(temp)
            for k in range(4):
                temp = 1/(1+np.exp(-net[k]))
                h.append(temp)
            for k in range(4):
                temp += h[k] *weight2[k]
                O = 1/(1+np.exp(-temp))
            for k in range(4):
                ntemp = -(y[j]-O)*O*(1-O)*h[k]
                temp1.append(ntemp)
            for k in range(4):
                ntemp = -(y[j]-O)*O*(1-O)*weight2[k]*h[k]*(1-h[k])*x[j]
                temp1.append(ntemp)
            E.append(temp1)
        for j in range(101):
            for k in range(8):
                if k <4:
                    weight2[k] -= 0.1 * E[j][k]
                else:
                    weight1[k-4] -= 0.1 * E[j][k]
    for i in range(101):
        O = 0
        h=[]
        net =[]
        for k in range(4):
            temp = weight1[k] * x[i]
            net.append(temp)
        for k in range(4):
            temp = 1 / (1 + np.exp(-net[k]))
            h.append(temp)
        for k in range(4):
            temp += h[k] * weight2[k]
            O = 1 / (1 + np.exp(-temp))
	print(O)
	result1.append(O)

iteration(500000)
print(weight1,weight2)
print(result1)

'''
f = open('result.csv','w')
wr =csv.writer(f)
for i in range(101):
    wr.writerow(result[i])

f.close()

'''