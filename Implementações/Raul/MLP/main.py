import numpy as np
from MLP import MLP
import random as rd
import math
import matplotlib. pyplot as plt
import pandas as pd
'''
## Create dataset
qtdRows = 100

data = np.random.rand(qtdRows,2)
classes = -1*np.ones((qtdRows,2))

new_data = np.random.rand(int(qtdRows*0.3),2)

## Function the define the classes
for row in range(qtdRows):
    if sum(data[row])**2 > 0.5:
        classes[row,0] = 1
    else:
        classes[row,1] = 1

real_classes = -1*np.ones((len(new_data),2))
for row in range(len(real_classes)):
    if sum(new_data[row])**2 > 0.5:
        real_classes[row,0] = 1
    else:
        real_classes[row,1] = 1
'''
x_train = pd.read_csv('Dataset/xtrain_3spirals.txt',sep='	', header = None)
x_test = pd.read_csv('Dataset/xtest_3spirals.txt',sep='	', header = None)

#converterClasses('Dataset/dtest_3spirals.txt')
#converterClasses('Dataset/dtrain_3spirals.txt')

d_train = pd.read_csv('Dataset/dtrain_3spirals.txt',sep=',', header = None)
d_test = pd.read_csv('Dataset/dtest_3spirals.txt',sep=',', header = None)


## Aplication of MLP algorithm
mlp = MLP(15000,0.15,0.000001,[4,3],0.5)
mlp.train(x_train.to_numpy(),d_train.to_numpy())

new_classes = mlp.application(x_test.to_numpy())

comparative = np.concatenate((d_test.to_numpy(),new_classes),1)

print("Matrix of comparative between classes")
print(comparative)

print("------------------------------")


hit_table = np.zeros((len(new_classes),1))
for row in range(len(new_classes)):
    if all(d_test.to_numpy()[row] == new_classes[row]):
        hit_table[row] = 1
    

tax_hit = sum(hit_table)/len(new_classes)

print("------------------------------")

print("Matrix of hits")
print(hit_table)

print("------------------------------")

print("Tax of hits: " + str(tax_hit) )
