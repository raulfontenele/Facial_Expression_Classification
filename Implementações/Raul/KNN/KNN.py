import numpy as np
import math

class KNN():
    def __init__(self,k_quant):
        self.k_nearst = k_quant
        self.data_base  = None
        self.data_class = None
    
    def fit(self,data,classific):
        if len(data) == len(classific):
            self.data_base = data
            self.data_class = classific
    
    def classifier(self,data_classifier):
        classes = -1*np.ones( (len(data_classifier),len(self.data_class[0])) )

        for row in range(len(data_classifier)):
            newData = self.DistMatrix(data_classifier[row])

            ## Sort matrix based on dist column
            index = np.argsort(newData[:,0])
            data_sorted = newData[index,:]
            k_fisrt = data_sorted[0:self.k_nearst,1:]

            ##Choose which class appears most
            index_most = np.argmax(sum(k_fisrt))
            classes[row][index_most] = 1
            '''
                ## Verificar a proporção de cada uma das classes.
            #sample_cl = [[-1,-1,-1],[-1,-1,1],[-1,1,-1],[-1,1,1],[1,-1,-1]]
            #sample_cl = np.array(sample_cl)
            count = np.array([0,0,0,0,0])
            for nrow in k_fisrt:
                for ind in range(5):
                    if np.array_equal(nrow,sample_cl[ind]):
                        count[ind]+=1
                        break
            classes[row,:] = sample_cl[np.argmax(count)]
            '''
        return classes

        
    def DistMatrix(self,data_point):
        dist_class = np.zeros( (len(self.data_base),1) )

        for index in range(len(self.data_base)):
            dist_class[index] =  math.sqrt( sum( (self.data_base[index] - data_point)**2) )
        dist_class = np.concatenate((dist_class,self.data_class),1)
        return dist_class