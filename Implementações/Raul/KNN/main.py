import numpy as np
from KNN import KNN
import random as rd
import math
import matplotlib. pyplot as plt

## Create dataset
qtdRows = 200

data = np.random.rand(qtdRows,2)
classes = np.zeros((qtdRows,2))

new_data = np.random.rand(int(qtdRows*0.3),2)

## Function the define the classes
for row in range(qtdRows):
    if sum(data[row])**2 > 0.5:
        classes[row,0] = 1
    else:
        classes[row,1] = 1

## Line that divide the classes
x = np.linspace(0,1,10)
y = math.sqrt(0.5) - x


## Aplication of KNN algorithm
knn = KNN(9)
knn.fit(data,classes)
new_classes = knn.classifier(new_data)

real_classes = np.zeros((len(new_classes),2))
for row in range(len(new_classes)):
    if sum(new_data[row])**2 > 0.5:
        real_classes[row,0] = 1
    else:
        real_classes[row,1] = 1

comparative = np.concatenate((real_classes,new_classes),1)

print("Matrix of comparative between classes")
print(comparative)

print("------------------------------")

print("Matrix of new data")
print(new_data)

hit_table = np.zeros((len(new_classes),1))
for row in range(len(new_classes)):
    if all(real_classes[row] == new_classes[row]):
        hit_table[row] = 1
    

tax_hit = sum(hit_table)/len(new_classes)

print("------------------------------")

print("Matrix of hits")
print(hit_table)

print("------------------------------")

print("Tax of hits: " + str(tax_hit) )



plt.plot(x,y,data[:,0],data[:,1],'ro',new_data[:,0],new_data[:,1],'b*')
plt.show()