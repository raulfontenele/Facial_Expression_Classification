import math
import time
import numpy as np
from my_AuxiliaryFunctions import my_AuxiliaryFunctions

class my_CQ():
    def __init__(self,Treino,Teste,Op,lb):
        
        self.LB = lb
        
        
        self.op = Op        
        self.xTreino  = Treino[:,0:2]
        self.RowsTr,self.ColTr = self.xTreino.shape
        self.xTeste = Teste[:,0:2]
        self.RowsT,self.ColT = self.xTeste.shape
        self.yTreino = Treino[:,2]
        self.yTreino.shape = (self.RowsTr,1)
        self.yTeste = Teste[:,2]
        self.yTeste.shape = (self.RowsT,1)
        self.ClassCounter =  int(np.max(self.yTreino))
        self.Centroides = [None] * self.ClassCounter
        self.MatricesByClass = [None] * self.ClassCounter
        self.CovMatrixbyClass = [None] * self.ClassCounter
        self.FriedmanCov = [None] * self.ClassCounter
        self.Inversas = [None] * self.ClassCounter
        self.Pooled = np.zeros((self.ColTr, self.ColTr))
        self.Distances = np.zeros((self.ClassCounter))
        self.Rotulado = np.array([])
        for i in range(self.ClassCounter):
            self.Centroides[i] = np.array([])
            self.MatricesByClass[i] = np.array([])
            self.CovMatrixbyClass[i] = np.array([])
            self.FriedmanCov[i] = np.array([])
            self.Inversas[i] = np.array([])

    def myCov(self,M):
        K,c = M.shape
        medio = sum(M)/K
        medio.shape = (1,c)
        sub = (M-np.tile(medio,(K,1))).T

        return 1/K * (sub @ sub.T)


    def PopulateMatrices(self):
        for i in range(self.ClassCounter):
            self.MatricesByClass[i].shape = (len(self.Centroides[i]),self.ColTr)

        for i in range(self.RowsTr):
            Sample =self.xTreino[i,0:self.ColTr]
            Sample.shape = (1,self.ColTr)
            self.MatricesByClass[int(self.yTreino[i][0]-1)] = np.concatenate((self.MatricesByClass[int(self.yTreino[i][0]-1)],Sample),axis=0)
        
        for i in range(self.ClassCounter):
            self.Centroides[i] =sum(self.MatricesByClass[i])/len(self.MatricesByClass[i])
            self.CovMatrixbyClass[i] = self.myCov(self.MatricesByClass[i])
            P_prior = len(self.MatricesByClass[i])/self.RowsTr
            self.Pooled+=(P_prior * self.CovMatrixbyClass[i])            
            Si = len(self.MatricesByClass) *  self.CovMatrixbyClass[i]
            self.FriedmanCov[i] = (((1-self.LB) * Si + self.LB * self.Pooled)/(((1-self.LB)*len(self.MatricesByClass))+0.75*self.RowsTr))

    def Run(self):
        Time = self.Treino()
        T_A,ConfMatrix = self.Teste()

        return T_A,Time,ConfMatrix
    
    def CalcDist(self,i):
        newSample = self.xTeste[i,:]
        newSample.shape = (1,self.ColT)
        for j in range(self.ClassCounter):
            self.Distances[j] = (newSample-self.Centroides[j]) @ self.Inversas[j] @ (newSample-self.Centroides[j]).T

        self.Rotulado = np.append(self.Rotulado,np.argmin(self.Distances)+1)

    def Treino(self):        
        start_time = time.time()        
        self.PopulateMatrices()
        if self.op == 1:
            IPooled = np.linalg.pinv(self.Pooled)
            for i in range(self.ClassCounter):
                self.Inversas[i] = IPooled

        elif self.op == 2:
            for i in range(self.ClassCounter):
                self.Inversas[i] = np.linalg.pinv(self.FriedmanCov[i])

        else:
            for i in range(self.ClassCounter):
                self.Inversas[i] = np.linalg.pinv(self.CovMatrixbyClass[i])
            
        for i in range(self.RowsT):
            self.CalcDist(i)

        return time.time() - start_time

    def Teste(self):
        hits =0 
        gestos = ["Neutro","Sorriso","Aberto","Surpreso","Grumpy"]
        M = np.zeros((len(gestos),len(gestos)))

        for i in range(self.RowsT):
            if(self.Rotulado[i]==self.yTeste[i]):
                M[int(self.yTeste[i])-1][int(self.Rotulado[i])-1] = M[int(self.yTeste[i])-1][int(self.Rotulado[i])-1]+1
                hits+=1
            else:
                M[int(self.yTeste[i])-1][int(self.Rotulado[i])-1] = M[int(self.yTeste[i])-1][int(self.Rotulado[i])-1]+1
                    
        cf = my_AuxiliaryFunctions()
        #cf.ConfMatrix(M)
        return hits/self.RowsT,M            