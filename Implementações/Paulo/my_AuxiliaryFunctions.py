import numpy as np
from my_KNN import my_KNN
import json
import locale
import csv
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

class my_AuxiliaryFunctions:
    def ConfMatrix(self,M,plotName):
        plotName+='.pdf'
        teste = M.astype(int)
        gestos = ["Neutro","Sorriso","Aberto","Surpreso","Grumpy"]

        
        df_cm = pd.DataFrame(teste, index = [i for i in gestos],
                  columns = [i for i in gestos])
        plt.figure(figsize = (10,7))
        
        sn.heatmap(df_cm, annot=True,fmt="d", annot_kws={"size": 14},cmap="YlGnBu")
        plt.savefig(plotName, bbox_inches='tight')
    def myK_Fold_CV(self,Data,K):
        list_KNN  = list(range(1,101,10))
        Desempenhos = np.zeros((len(list_KNN), 2))
        z=0
        for KN in list_KNN:            
            FirstLimit = 0
            sumD = 0
            Partitions = [None] * K
            Data_partition = len(Data)//K
            LastLimit = Data_partition
            for i in range(len(Partitions)):
                if (i!=K-1):
                    Partitions[i] = Data[FirstLimit:LastLimit,:]
                    FirstLimit+=Data_partition
                    LastLimit+=Data_partition
                else:
                    Partitions[i] = Data[FirstLimit:len(Data),:]
            
            for i in range(len(Partitions)):                
                aux = list(range(len(Partitions)))
                aux.remove(i)
                Teste = Partitions[i]
                Treino = Partitions[aux[0]]
                aux.pop(0)            
                for j in aux:                
                    Treino = np.concatenate((Treino,Partitions[j]),axis=0)
                    
                knn=my_KNN(Treino,Teste,KN+1)
                
                T_A,Tempo =knn.Run()
                sumD+=T_A
            
            Desempenhos[z][0] = sumD/len(Partitions)
            Desempenhos[z][1] = KN
            z+=1
        print(Desempenhos)
        return Desempenhos[int(np.argmax(Desempenhos[:,0]))][1]


    def InserirRelatorioMLP(self,parametros):
        for i in range(len(parametros)):            
            if i<len(parametros)-1:
                parametros[i] = str(parametros[i]).replace(".",",")
            

        locale.setlocale(locale.LC_ALL, '')
        DELIMITER = ';' if locale.localeconv()['decimal_point'] == ',' else ','
        with open('relatorio.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=DELIMITER)
            writer.writerows([parametros])
        

    def InserirRelatorio(self,parametros): 
        for i in range(len(parametros)):            
            parametros[i] = str(parametros[i]).replace(".",",")       

        locale.setlocale(locale.LC_ALL, '')
        DELIMITER = ';' if locale.localeconv()['decimal_point'] == ',' else ','
        with open(parametros[0]+'.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=DELIMITER)
            writer.writerows([parametros])
    
    def MinMax(self,M):
        aux = M[:,2]
        aux.shape = (len(aux),1)
        newM = M[:,0:2]
        mini = np.min(newM)
        maxi = np.max(newM)
        r,c = newM.shape
        rows = list(range(0, r))
        col = list(range(0, c))
        for i in rows:
            for j in col:
                newM[i][j]  = (newM[i][j] - mini)/(maxi-mini)

        newM = np.concatenate((newM,aux),axis=1)
        return newM

    def RetrieveDataSet(self,FileName):
        #FileName = "TrainingTestData.json"
        FileName = FileName+'.json'
        gestures = ['Neutro', 'Sorriso','Aberto','Surpreso','Grumpy']
        f = open(FileName)
        data = json.load(f)
        f.close()    
        Pred1 = np.array([])
        Pred2 = np.array([])
        Rot = np.array([])
        mul =1
        for i in gestures:
            s1 = np.asarray(data['Data'][i][0])
            Pred1 = np.concatenate((Pred1,s1),axis=0)
            s2 = np.asarray(data['Data'][i][1])
            Pred2 = np.concatenate((Pred2,s2),axis=0)
            Rotulos = np.multiply(np.ones(len(s2)),mul)
            mul+=1
            Rot = np.concatenate((Rot,Rotulos),axis=0)
        Pred1.shape = (len(Pred1),1)
        Pred2.shape = (len(Pred2),1)
        Rot.shape = (len(Rot),1)     

        return np.concatenate((Pred1,Pred2,Rot),axis=1) 