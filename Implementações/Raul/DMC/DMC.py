import numpy as np
import math

class DMC():
    def __init__(self):
        self.data_base  = None
        self.data_class = None
        self.centroid_coord = []
    
    def fit(self,data,classific):
        if len(data) == len(classific):
            self.data_base = data
            self.data_class = classific
            self.calculateCentroid()
        print("coord_Centroides")
        print(self.centroid_coord)
    
    def classifier(self,data_classifier):
        classes = -1 * np.ones( (len(data_classifier),len(self.data_class[0])) )

        for row in range(len(data_classifier)):
            ## Calcule distances to centroid
            dist = np.zeros((len(self.data_class[0])))
            for n_centr in range(len(self.data_class[0])):
                dist[n_centr] = math.sqrt( sum( (self.centroid_coord[n_centr] - data_classifier[row][:])**2) )
            
            ## Get index of the lowest value of the vector
            index = np.argmin(dist)
            classes[row][index] = 1
        
        return classes
       

    def calculateCentroid(self):
        numb_classes = len(self.data_class[0])
        class_elements = []
        for index_class in range(numb_classes):
            auxClass = []
            class_elements.append (auxClass)

        ## Agrupando classes
        for index in range(len(self.data_base)):
            for index_class in range(numb_classes):
                if self.data_class[index][index_class] == 1:
                    class_elements[index_class].append(self.data_base[index])
        ## Calculando o centroide
        for index_class in range(numb_classes):
            self.centroid_coord.append( sum(class_elements[index_class])/len(class_elements[index_class])  )
        

    
