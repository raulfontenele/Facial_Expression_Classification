import math
import time
import numpy as np
from my_AuxiliaryFunctions import my_AuxiliaryFunctions

class my_KNN():
    def __init__(self,Treino,Teste,K):        
        self.K = K
        self.xTreino  = Treino[:,0:2]
        self.xTeste = Teste[:,0:2]
        self.yTreino = Treino[:,2]
        self.yTeste = Teste[:,2]              
        self.ClassCounter=int(np.max(self.yTreino))
        self.countRotulos = np.zeros((self.ClassCounter))
        self.pr = np.zeros((self.ClassCounter))
        self.Amostras = len(self.yTeste)
        self.Rotulado = np.zeros((len(self.yTeste)))
        self.Distances = np.zeros((len(self.xTreino))) 

    def Run(self):        
        Time = self.Treino()
        T_A = self.Teste()        
        return T_A,Time                
    
    def DistCalc(self,i):        
        for j in range(len(self.xTreino)):
            self.Distances[j] = math.sqrt(sum((self.xTreino[j,:] - self.xTeste[i,:])**2))                                
    
    def Treino(self):
        start_time = time.time()
        for i in range(self.Amostras):
            self.DistCalc(i)
            K_minors = np.argsort(self.Distances)[:self.K]            
            self.countRotulos = np.zeros((self.ClassCounter))
            for j in K_minors:
                self.countRotulos[int(self.yTreino[j]-1)]+=1  

            self.pr = np.zeros((self.ClassCounter))
            for j in range(self.ClassCounter):
                self.pr[j] = self.countRotulos[j]/self.K            
            self.Rotulado[i] = np.argmax(self.countRotulos)+1 

        return time.time()-start_time

    def Teste(self):
        hits = 0
        gestos = ["Neutro","Sorriso","Aberto","Surpreso","Grumpy"]
        M = np.zeros((len(gestos),len(gestos)))
        for i in range(self.Amostras):
            if(self.Rotulado[i]==self.yTeste[i]):
                M[int(self.yTeste[i])-1][int(self.Rotulado[i])-1] = M[int(self.yTeste[i])-1][int(self.Rotulado[i])-1]+1
                hits+=1
            else:
                M[int(self.yTeste[i])-1][int(self.Rotulado[i])-1] = M[int(self.yTeste[i])-1][int(self.Rotulado[i])-1]+1
        cf = my_AuxiliaryFunctions()
        cf.ConfMatrix(M)
        
        return hits/self.Amostras
            