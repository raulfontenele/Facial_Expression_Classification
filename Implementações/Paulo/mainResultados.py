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
    Treino = mAF.RetrieveDataSet('TrainingTestData')
    #np.random.shuffle(DataSet)
    Rep = 50
    ListTestSets = [None] * Rep

    for i in range(Rep):
        AuxiliaryCodes.ReturnDataMatrix(500)
        DataSet = mAF.RetrieveDataSet('FinalTestDS')
        #np.random.shuffle(DataSet)
        ListTestSets[i] = DataSet
    

   
    
    #KNN: 
    print("KNN:")
    K = [11,21]
    for j in range(Rep):
        print("COMEÇOU rodada "+str(j))
        for i in K:
            print("PARA k="+str(i))                
            knn=my_KNN(Treino,ListTestSets[j],int(i))
            T_A,Tempo =knn.Run()
            mAF.InserirRelatorio(['KNN_Resultados',int(i),T_A,Tempo])

    
    #CQ:
    #1: Agregada
       
    print("COMEÇOU CQ AGREGADA")    
    for i in range(Rep):
        cq = my_CQ(Treino,ListTestSets[i],1,1)
        T_A,Tempo = cq.Run()
        mAF.InserirRelatorio(['CQAg','Agregada',T_A,Tempo])
    
    
    #2: Friedman
    Lambda = 0.2
    ConfM = []
    MediConf = np.zeros((5,5))
    print("CQ FRIEDMAN ") 
     
    for i in range(Rep):            
        cq = my_CQ(Treino,ListTestSets[i],2,Lambda)
        T_A,Tempo,M = cq.Run()
        mAF.ConfMatrix(M,("CQ_ConfM"+str(i)))
        MediConf+=M

        mAF.InserirRelatorio(['CQFR_resultados_final2','Friedman',Lambda,T_A,Tempo])
    
    MediConf /=  Rep
    mAF.ConfMatrix(MediConf,"MediaCQ")

    
    #MLP         Treino,Teste,Topology,MaxEpoch,LR,Precision
    

    

    

    #topo = [[5],[7],[9],[11],[13],[15],[17],[19],[21],[23],[31],[41],[51],[101],[201],[401]]
    
    #for i in range(300, 800, 10):
    #   topo.append([i])
    #topo = [[5,5],[7,7],[9,9],[11,11],[13,13],[15,15],[17,17],[19,19],[21,21],[23,23],[31,31],[41,41],[51,51],[101,101],[201,201],[401,401]]
    
    topo = [[5],[9],[5,5],[9,9]]
    mlp = my_MLP1(Treino,ListTestSets[j],topo[i],12000,0.2,0.000001)
    for i in range(len(topo)):
        for j in range(50):
            

            mlp = my_MLP1(Treino,ListTestSets[j],topo[i],12000,0.2,0.000001)
            T_A,Tempo,Epoch,Hist = mlp.Run()
            print("RODADA"+str(i))
            print("Topologia: "+str(topo[i]))
            print("T_A:"+str(T_A) + " Epoca: "+str(Epoch))            
            print("-------------------------------------")
            mAF.InserirRelatorio(['MLP_resultados',str([topo[i],Epoch]),T_A,Tempo])
            
        
    








Main()