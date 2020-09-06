import math
import time
import numpy as np
import random as rand
from numpy import random
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from mpl_toolkits.mplot3d import Axes3D

class my_MLP1():   

    def __init__(self,Treino,Teste,Topology,MaxEpoch,LR,Precision):
        self.Top = Topology
        self.MaxEpoch = MaxEpoch
        self.LR = LR
        self.precision = Precision

        self.xTreino = Treino[:,0:2]
        self.r,self.c = self.xTreino.shape
        self.xTeste = Teste[:,0:2]
        self.rt,self.ct = self.xTeste.shape    
        self.yTreino = Treino[:,2]
        self.yTreino.shape = (len(self.yTreino),1)
        self.yTeste = Teste[:,2]
        self.yTeste.shape = (len(self.yTeste),1)
        self.Count_class = int(max(self.yTreino))

        self.I=[]
        self.Y=[]
        self.line =[]
        self.Y_rotulado = [] 
        self.AtualWeights = [None] * int(len(self.Top)+1)
        self.Accumuladores = [None] * int(len(self.Top)+1)
        self.Epoch = 0
        self.MSE1 = 0
        self.MSE2 = self.precision+1
        self.ArrAux = np.array([-1])
        self.ArrAux.shape = (1,1)
        self.erro = 0


        self.yTrainMatrix = self.GenerateYtrain(self.yTreino)
        self.BiasedXtrain = self.BiasGenerator(self.xTreino)
        self.BiasedXTest = self.BiasGenerator(self.xTeste)
        self.yTesteMatrix = self.GenerateYtrain(self.yTeste)

        for i in range(len(self.AtualWeights)):
            if i==0:
                self.AtualWeights[i] = random.rand(self.Top[i],self.c+1)-0.5
                self.Accumuladores[i] = np.zeros((self.Top[i],self.c+1))
                #self.AtualWeights[i] = np.zeros((self.Top[i],self.c+1))-0.5
            elif (i>0 and i<len(self.AtualWeights)-1):
                self.AtualWeights[i] = random.rand(self.Top[i],self.Top[i-1]+1)-0.5
                self.Accumuladores[i] = np.zeros((self.Top[i],self.Top[i-1]+1))
                #self.AtualWeights[i] = np.zeros((self.Top[i],self.Top[i-1]+1))-0.5
            else:
                self.AtualWeights[i] = random.rand(self.Count_class,self.Top[i-1]+1)-0.5
                #self.AtualWeights[i] = np.zeros((self.Count_class,self.Top[i-1]+1))-0.5     
                self.Accumuladores[i] = np.zeros((self.Count_class,self.Top[i-1]+1))        

    def __del__(self):
        print ("deleted")
    def GenerateYtrain(self,M):                    
        v = (np.ones((self.Count_class,self.Count_class))*-1)+np.eye(self.Count_class)*2        
        BigMatrix = [None] * int(len(M))        
        for i in range(len(M)):
            BigMatrix[i] = v[int(M[i]-1)]
        
        return BigMatrix

    def BiasGenerator(self,M):
        aux = np.ones((len(M),1))*-1
        aux.shape = (len(M),1)
        Matrix = np.concatenate((aux,M),axis=1) 
        return Matrix

    def ClearACC(self):        
        for i in range(len(self.AtualWeights)):
            if i==0:                
                self.Accumuladores[i] = np.zeros((self.Top[i],self.c+1))
            elif (i>0 and i<len(self.AtualWeights)-1):                
                self.Accumuladores[i] = np.zeros((self.Top[i],self.Top[i-1]+1))
            else:                
                self.Accumuladores[i] = np.zeros((self.Count_class,self.Top[i-1]+1))

    def TanHDerivative(self,x):           
        return 1-np.power(np.tanh(x), 2) 
    
    def Feed(self,i):        
        for j in range(len(self.AtualWeights)):
            if j==0:                
                Sample = self.BiasedXtrain[i,:]
                Sample.shape = (len(Sample),1)
                Is = self.AtualWeights[j]@Sample                        
                self.I.append(Is)        
                Ys = np.concatenate((self.ArrAux,np.tanh(Is)),axis=0)                     
                self.Y.append(Ys)
            elif (j>0 and j<len(self.AtualWeights)-1):   
                Is = self.AtualWeights[j]@Ys
                Ys = np.concatenate((self.ArrAux,np.tanh(Is)),axis=0) 
                self.I.append(Is)  
                self.Y.append(Ys)                
            else:  
                Is = self.AtualWeights[j]@Ys                                   
                self.I.append(Is)  
                self.Y.append(np.tanh(Is))
                self.line = self.yTrainMatrix[i]
                self.line.shape = (len(self.line),1)
                self.erro = self.erro + (np.power(sum(self.line-np.tanh(Is)), 2)/2)              
                
                
                
                
    def Back(self,i):
    #  it = reversed(range(len(self.AtualWeights)))
        for j in reversed(range(len(self.AtualWeights))):
            if j==len(self.AtualWeights)-1:   
                self.Accumuladores[j] = self.Accumuladores[j] + ((self.LR * ((self.line-self.Y[j])*self.TanHDerivative(self.I[j])) )@self.Y[j-1].T)
                m,n = self.AtualWeights[j].shape
                Prod = self.AtualWeights[j][:,1:n].T@((self.line-self.Y[j])*self.TanHDerivative(self.I[j]))
            elif (j<len(self.AtualWeights)-1 and j>0):                                    
                self.Accumuladores[j] = self.Accumuladores[j]+ ((self.LR* (Prod*self.TanHDerivative(self.I[j])) ) @ self.Y[j-1].T)
                m,n = self.AtualWeights[j].shape                
                Prod = self.AtualWeights[j][:,1:n].T @ (Prod*self.TanHDerivative(self.I[j]))
            else:                
                xbias = self.BiasedXtrain[i,:]
                xbias.shape = (1,len(xbias))
                self.Accumuladores[j] = self.Accumuladores[j]+ ((self.LR*(Prod*self.TanHDerivative(self.I[j]))) @ xbias) 

    def FeedBack(self):              
        for i in range(self.r):  
            self.I = []
            self.Y = []
            self.Feed(i)
            self.Back(i)

    def AtualizarPesos(self):        
        for i in range(len(self.AtualWeights)):        
            self.AtualWeights[i] = self.AtualWeights[i] + (self.Accumuladores[i]/self.r)

    def CalculoErro(self):
        self.erro = 0 
               
        for i in range(self.r):
            self.Feed(i)            
        
        return self.erro[0]/self.r


    def Treino(self):
        start_time = time.time()
        histMSE = []
          
        
        while((self.Epoch<self.MaxEpoch)and(abs(self.MSE2-self.MSE1)>self.precision)):                        
            self.ClearACC()
            self.MSE1 = self.MSE2
            self.FeedBack()
            self.AtualizarPesos()
            self.MSE2 = self.CalculoErro()
            self.Epoch+=1
            histMSE.append(self.MSE2) 
            #print("Epoca:"+str(self.Epoch))
            #print("MSE:"+str(self.MSE2))
            #print("ABS:"+str(np.abs(self.MSE2-self.MSE1)))
            #print("-----------------")
                        
        return (time.time() - start_time),self.Epoch,histMSE
    def FeedTeste(self,i):
        for j in range(len(self.AtualWeights)):
            if j==0:                
                Sample = self.BiasedXTest[i,:].T
                Sample.shape = (len(Sample),1)                                  
                Ys = np.concatenate((self.ArrAux,np.tanh(self.AtualWeights[j]@Sample)),axis=0)                     
                
            elif (j>0 and j<len(self.AtualWeights)-1):                                
                Ys = np.concatenate((self.ArrAux,np.tanh(self.AtualWeights[j]@Ys)),axis=0) 
            else:     
                self.Y_rotulado.append(np.tanh(self.AtualWeights[j]@Ys).T)

    def Teste(self):
        self.Y_rotulado = []                  
        for i in range(self.rt):            
            self.FeedTeste(i)

        hits = 0
        for i in range(len(self.Y_rotulado)):
            posP = np.argmax(self.Y_rotulado[i])
            posR = np.argmax(self.yTesteMatrix[i])
            if(posP==posR):
                hits+=1

        return hits/self.rt
    
    def ErrorPlot(self,Error,Epoch):
        PlotName = str(self.Top)+"MSE.pdf"        
        plt.plot(Error , label='MSE')        
        #plt.xticks(np.arange(0, Epoch, step=1))
        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
                ncol=2, mode="expand", borderaxespad=0.)        
        plt.savefig(PlotName, bbox_inches='tight')
        plt.close()

    def Run(self):
        Time,Epoch,Hist = self.Treino()
        self.ErrorPlot(Hist,Epoch)        
        print("Fim treino em:"+str(Epoch)+" epocas e "+str(Time)+"s"+" MSE final: "+str(self.MSE2))
        T_A = self.Teste()
        return T_A,Time,Epoch,Hist
