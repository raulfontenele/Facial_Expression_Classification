from my_KNN import my_KNN
from my_DMC import my_DMC
from my_LMQ import my_LMQ
from my_CQ import my_CQ
from my_MLP import my_MLP
from my_MLP1 import my_MLP1
from my_AuxiliaryFunctions import my_AuxiliaryFunctions
from pdf2image import convert_from_path
import requests
import myGraphics
import json
import AuxiliaryCodes   
import time
import my_classifiers
import csv
import locale
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from mpl_toolkits.mplot3d import Axes3D



def Main(): 
    mAF = my_AuxiliaryFunctions()
    #conjunto de dados.    
    DataSet = mAF.RetrieveDataSet('FinalTestDS')
    np.random.shuffle(DataSet)
    #K fold para achar o K do KNN.
    #ChosenOne = mAF.myK_Fold_CV(DataSet,10)
    
    #ChosenOne = 1.0
    #print("K escolhido foi:"+str(ChosenOne)) 


    Treino  = DataSet[0:int(len(DataSet)*.8),:]
    Teste = DataSet[int(len(DataSet)*.8):int(len(DataSet)),:]
    Rep = 50
    #TrainingTestData
    DataSet = mAF.RetrieveDataSet('TrainingTestData')
    np.random.shuffle(DataSet)
    
    M = AuxiliaryCodes.RetrieveFixedDS()
    
    ListDS = [None] * Rep
    for i in range(Rep):

        DataSet = mAF.RetrieveDataSet('TrainingTestData')
        np.random.shuffle(DataSet)
        ListDS[i] = DataSet
    '''
    #TESTE MLP1:
    DataSet1 = mAF.MinMax(M)
    Treino  = DataSet1[0:int(len(DataSet1)*.8),:]
    Teste = DataSet1[int(len(DataSet1)*.8):int(len(DataSet1)),:]
    mlp = my_MLP1(Treino,Teste,[5,5],12000,0.2,0.000001)            
    T_A,Tempo,Epoch,Hist = mlp.Run()
    bp=1
        
    
    #KNN: 
    K = [1,11,21,31,41,51,61,71,81,91]
    for i in K:
        print("PARA k="+str(i))        
        for j in range(100):
            print("COMEÇOU rodada "+str(j))    
            DataSet = mAF.RetrieveDataSet()
            np.random.shuffle(DataSet)        
            Treino  = DataSet[0:int(len(DataSet)*.8),:]
            Teste = DataSet[int(len(DataSet)*.8):int(len(DataSet)),:]
            knn=my_KNN(Treino,Teste,int(i))
            T_A,Tempo =knn.Run()
            mAF.InserirRelatorio(['KNN',int(i),T_A,Tempo])
    
    
    #DMC:
    print("COMEÇOU DMC")    
    for i in range(Rep):
        Treino  = ListDS[i][0:int(len(ListDS[i])*.8),:]
        Teste = ListDS[i][int(len(ListDS[i])*.8):int(len(DataSet)),:]
        dmc = my_DMC(Treino,Teste)
        T_A,Tempo = dmc.Run()
        mAF.InserirRelatorio(['DMC','campo vazio',T_A,Tempo])
    
    
    #LQM:
    print("COMEÇOU LQM COM TIKHONOV")  
    Lambda = np.arange(0, 1, 0.05)    
    print(Lambda)
    for j in Lambda:
        for i in range(Rep):
            DataSet = mAF.RetrieveDataSet()
            np.random.shuffle(DataSet)        
            Treino  = DataSet[0:int(len(DataSet)*.8),:]
            Teste = DataSet[int(len(DataSet)*.8):int(len(DataSet)),:]
            lmq = my_LMQ(Treino,Teste,[True,j])
            T_A,Tempo = lmq.Run()
            mAF.InserirRelatorio(['LQMTIK',['Tikhonov:',True],j,T_A,Tempo])
    
    #LQM:
    print("COMEÇOU LQM SEM TIKHONOV")    
    for i in range(Rep):
        DataSet = mAF.RetrieveDataSet()
        np.random.shuffle(DataSet)        
        Treino  = DataSet[0:int(len(DataSet)*.8),:]
        Teste = DataSet[int(len(DataSet)*.8):int(len(DataSet)),:]
        lmq = my_LMQ(Treino,Teste,[False,0.6])
        T_A,Tempo = lmq.Run()
        mAF.InserirRelatorio(['LQM',['Tikhonov:',False],T_A,Tempo])
        
    
    DataSet = mAF.RetrieveDataSet()
    np.random.shuffle(DataSet)
    #cq = my_CQ(Treino,Teste,2,0.2)
    #T_A,Tempo = cq.Run()
    knn=my_KNN(Treino,Teste,1)
    T_A,Tempo =knn.Run()

    #CQ:
    #1: Agregada
    Lambda = np.arange(0, 1, 0.05)   
    print("COMEÇOU CQ AGREGADA")    
    for i in range(Rep):
        DataSet = mAF.RetrieveDataSet()
        np.random.shuffle(DataSet)        
        Treino  = DataSet[0:int(len(DataSet)*.8),:]
        Teste = DataSet[int(len(DataSet)*.8):int(len(DataSet)),:]
        cq = my_CQ(Treino,Teste,1,1)
        T_A,Tempo = cq.Run()
        mAF.InserirRelatorio(['CQAg','Agregada',T_A,Tempo])
    
    #2: Friedman
    print("COMEÇOU CQ FRIEDMAN ") 
    for j in Lambda: 
        for i in range(Rep):
            DataSet = mAF.RetrieveDataSet()
            np.random.shuffle(DataSet)        
            Treino  = DataSet[0:int(len(DataSet)*.8),:]
            Teste = DataSet[int(len(DataSet)*.8):int(len(DataSet)),:]
            cq = my_CQ(Treino,Teste,2,j)
            T_A,Tempo = cq.Run()
            mAF.InserirRelatorio(['CQFR','Friedman',j,T_A,Tempo])
    #3: Covariância das classes
    print("COMEÇOU CQ LIMPA E SECA")  
    for i in range(Rep):
        DataSet = mAF.RetrieveDataSet()
        np.random.shuffle(DataSet)        
        Treino  = DataSet[0:int(len(DataSet)*.8),:]
        Teste = DataSet[int(len(DataSet)*.8):int(len(DataSet)),:]
        cq = my_CQ(Treino,Teste,3,1)
        T_A,Tempo = cq.Run()
        mAF.InserirRelatorio(['CQ','Sem Reg',T_A,Tempo])

        
    '''
    #MLP         Treino,Teste,Topology,MaxEpoch,LR,Precision
    print("COMEÇOU O Mega Lento Perceptron ") 

    

    

    #topo = [[5],[7],[9],[11],[13],[15],[17],[19],[21],[23],[31],[41],[51],[101],[201],[401]]
    topo=[]
    for i in range(7, 550, 3):
        topo.append([i])
    #topo = [[5,5],[7,7],[9,9],[11,11],[13,13],[15,15],[17,17],[19,19],[21,21],[23,23],[31,31],[41,41],[51,51],[101,101],[201,201],[401,401]]

    for i in range(len(topo)):
        for j in range(3):
            print("RODADA ["+str(i)+"] ["+str(j)+"]")
            print("-------------------------------------")
            print("TOPOLOGIA:"+str(topo[i]))
            DataSet = mAF.RetrieveDataSet('TrainingTestData')
            np.random.shuffle(DataSet)
            x = DataSet[:,1]
            DataSet1 = mAF.MinMax(DataSet)
            x = DataSet1[:,1]
            Treino  = DataSet1[0:int(len(DataSet1)*.8),:]
            Teste = DataSet1[int(len(DataSet1)*.8):int(len(DataSet1)),:]

            print("MLP classe:")
            mlp = my_MLP1(Treino,Teste,topo[i],15000,0.2,0.000001)            
            T_A,Tempo,Epoch,Hist = mlp.Run()    
            mAF.InserirRelatorio(['MLP',str([topo[i],Epoch]),T_A,Tempo])
            print("Topologia: "+str(topo[i]))
            print("T_A:"+str(T_A) + " Epoca: "+str(Epoch))            
            print("Tempo treino:"+str(Tempo))
            print("-------------------------------------")            
            
            del mlp
        









Main()