import math
import time
import numpy as np

class my_LMQ():
    def __init__(self,Treino,Teste,Tikhonov):
        self.lbd = Tikhonov[1]
        self.Tik = Tikhonov[0]        
        self.xTreino  = Treino[:,0:2]
        self.RowsTr,self.ColTr = self.xTreino.shape
        self.xTeste = Teste[:,0:2]
        self.RowsT,self.ColT = self.xTeste.shape
        self.yTreino = Treino[:,2]
        self.yTreino.shape = (self.RowsTr,1)
        self.yTeste = Teste[:,2]
        self.yTeste.shape = (self.RowsT,1)
        self.ClassCounter =  int(np.max(self.yTreino))
        self.W = np.array([])        
        self.RotulosTreino = np.ones((self.ClassCounter,self.RowsTr))*-1
        self.RotulosTeste = np.ones((self.ClassCounter,self.RowsT))*-1
        for i in range(self.RowsTr):
            rotulo = int(self.yTreino[i][0])
            self.RotulosTreino[rotulo-1][i]=1
        for i in range(self.RowsT):
            rotulo = int(self.yTeste[i][0])
            self.RotulosTeste[rotulo-1][i]=1

    def Run(self):
        Time = self.Treino()
        T_A = self.Teste()

        return T_A,Time
    
    
    def Treino(self):        
        start_time = time.time()
        if(self.Tik):
            self.W = self.RotulosTreino @ self.xTreino @ (np.linalg.pinv((self.xTreino.T @ self.xTreino) + (self.lbd * np.eye(self.ColTr))))
        else:
            self.W = self.RotulosTreino @ self.xTreino @ (np.linalg.pinv(self.xTreino.T @ self.xTreino))

        return time.time() - start_time

    def Teste(self):
        Y_hat = self.W @ self.xTeste.T        
        hits =0
        r,c = Y_hat.shape
        for i in range(c):
            rotulado = np.ones((self.ClassCounter,1))*-1
            rotulado[np.argmax(Y_hat[:,i])][0]=1
            rotulo = self.RotulosTeste[:,i]
            rotulo.shape = (len(rotulo),1)
            if(np.array_equal(rotulado,rotulo)):
                hits+=1            
        
        return hits/self.RowsT    
    