import math
import time
import numpy as np

class my_DMC():
    def __init__(self,Treino,Teste):
        self.xTreino  = Treino[:,0:2]
        self.RowsTr,self.ColTr = self.xTreino.shape
        self.xTeste = Teste[:,0:2]
        self.RowsT,self.ColT = self.xTeste.shape
        self.yTreino = Treino[:,2]
        self.yTreino.shape = (len(self.yTreino),1)
        self.yTeste = Teste[:,2]
        self.yTeste.shape = (len(self.yTeste),1)
        self.ClassCounter=int(np.max(self.yTreino))
        self.ClassLoop = list(range(0,int(self.ClassCounter)))                      
        self.Rotulado = np.zeros((len(self.yTeste)))
        self.Distances = np.zeros((self.ClassCounter))
        self.Centroides = [None] * int(self.ClassCounter)      

    def Run(self):
        Time = self.Treino()
        T_A = self.Teste()
        return T_A,Time
    
    def DistCalc(self,i):        
        for j in self.ClassLoop:                                            
            self.Distances[j] = math.sqrt(sum((self.Centroides[j] - self.xTeste[i,:])**2))
    
    def GenerateCentroids(self):
        for i in self.ClassLoop:            
            self.Centroides[i] = np.array([])
            self.Centroides[i].shape = (len(self.Centroides[i]),self.ColTr)
        for j in range(self.RowsTr):
            aux = self.xTreino[j,0:self.ColTr]
            aux.shape = (1,self.ColTr)              
            self.Centroides[int(self.yTreino[j][0]-1)] = np.concatenate((self.Centroides[int(self.yTreino[j][0]-1)],aux),axis=0)
        for i in self.ClassLoop:
            self.Centroides[i] =np.sum(self.Centroides[i], axis = 0)/len(self.Centroides[i])
    
    def Treino(self):        
        start_time = time.time()
        self.GenerateCentroids()
        for i in range(self.RowsT):
            self.DistCalc(i)
            pos = np.argmin(self.Distances)            
            self.Rotulado[i] = pos+1

        return time.time()-start_time

    def Teste(self):
        hits =0
        for i in range(self.RowsT):
            if (self.yTeste[i]==self.Rotulado[i]):
                hits+=1
        
        return hits/self.RowsT




        

  
    
    
    
    
    
    
    
    