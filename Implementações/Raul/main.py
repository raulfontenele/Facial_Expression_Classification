from AuxFunctions.ImportData import importacao,importacaoCompleta
from AuxFunctions.InsertReport import InserirRelatorio
from AuxFunctions.createDatasetTest import DatasetTest
from KNN.KNN import KNN
from MLP.MLP import MLP
from DMC.DMC import DMC
import numpy as np
from datetime import datetime
import matplotlib. pyplot as plt


def Main():
    '''
    ## primeira etapa de execuções

    ## Aplication of KNN algorithm
    for ind in [101,111,121,131,141]:
        for i in range(90):
            x_train,x_test,d_train,d_test = importacao('../AquisicaoDados/DataSet/TrainingTestData.json')

            startTime = datetime.now()
            knn = KNN(ind)
            knn.fit(x_train,d_train)
            new_classes = knn.classifier(x_test)
            stopTime = datetime.now()

            hit_table = np.zeros((len(new_classes),1))
            for row in range(len(new_classes)):
                if all(d_test[row] == new_classes[row]):
                    hit_table[row] = 1

            tax_hit = sum(hit_table)/len(new_classes)
            print(tax_hit)
            
            InserirRelatorio(['KNN',ind,float(tax_hit),stopTime-startTime])

    ## Aplication of DCM algorithm
    for i in range(50):
        x_train,x_test,d_train,d_test = importacao('../AquisicaoDados/DataSet/TrainingTestData.json')

        startTime = datetime.now()
        dcm = DMC()
        dcm.fit(x_train,d_train)
        new_classes = dcm.classifier(x_test)
        stopTime = datetime.now()

        hit_table = np.zeros((len(new_classes),1))
        for row in range(len(new_classes)):
            if all(d_test[row] == new_classes[row]):
                hit_table[row] = 1

        tax_hit = sum(hit_table)/len(new_classes)
        print(tax_hit)
        
        InserirRelatorio(['DCM','-',float(tax_hit),stopTime-startTime])

'''
    for j in range(2):
        ## Aplication of MLP algorithm
        topologias = [[15,15],[17,17]]
        for i in range(len(topologias)):
            x_train,x_test,d_train,d_test = importacao('../AquisicaoDados/DataSet/TrainingTestData.json')
            startTime = datetime.now()

            mlp = MLP(12000,0.2,0.000001,topologias[i],500)
            epocas,histEqm = mlp.train(x_train,d_train)
            
            plt.figure()
            plt.plot(np.arange(len(histEqm)),histEqm)
            plt.xlabel('Quantidade de épocas')
            plt.ylabel('Erro quadrático médio')
            plt.title("EQM x Épocas")
            plt.savefig('plots/'+ str(topologias[i]) + '-Execucao' + str(j) + '.png')
            plt.close()


            new_classes = mlp.application(x_test)   

            stopTime = datetime.now()
            hit_table = np.zeros((len(new_classes),1))
            for row in range(len(new_classes)):
                if all(d_test[row] == new_classes[row]):
                    hit_table[row] = 1
                

            tax_hit = sum(hit_table)/len(new_classes)

            print("Tax of hits: " + str(tax_hit) )
            InserirRelatorio(['MLP',topologias[i],float(tax_hit),stopTime-startTime,epocas])

    ## Segunda etapa de execuções
    '''
    ## Aplication of KNN algorithm
    for ind in [1,11]:
        for i in range(50):
            x_train,d_train = importacaoCompleta('../AquisicaoDados/DataSet/TrainingTestData.json')
            x_test,d_test = DatasetTest(500)

            startTime = datetime.now()
            knn = KNN(ind)
            knn.fit(x_train,d_train)
            
            new_classes = knn.classifier(x_test)
            stopTime = datetime.now()

            hit_table = np.zeros((len(new_classes),1))
            for row in range(len(new_classes)):
                if all(d_test[row] == new_classes[row]):
                    hit_table[row] = 1

            tax_hit = sum(hit_table)/len(new_classes)
            print(tax_hit)
            
            InserirRelatorio(['KNN',ind,i,float(tax_hit),stopTime-startTime])
'''
'''
    ## Aplication of MLP algorithm

    topologias = [[70,70]]
    for i in range(len(topologias)):
        x_train,d_train = importacaoCompleta('../AquisicaoDados/DataSet/TrainingTestData.json')
        startTime = datetime.now()

        mlp = MLP(14000,0.2,0.000001,topologias[i],500)
        epocas,histEqm = mlp.train(x_train,d_train)

        stopTime = datetime.now()

        ## Aplicar em 50 datasets diferentes e calcular as taxas de acerto
        for n in range(50):

            x_test,d_test = DatasetTest(500)

            new_classes = mlp.application(x_test)   

            stopTime = datetime.now()
            hit_table = np.zeros((len(new_classes),1))
            for row in range(len(new_classes)):
                if all(d_test[row] == new_classes[row]):
                    hit_table[row] = 1
                

            tax_hit = sum(hit_table)/len(new_classes)

            print("Tax of hits: " + str(tax_hit) )
            InserirRelatorio(['MLP',topologias[i],n,float(tax_hit),stopTime-startTime,epocas])

'''    
'''
#x_train,x_test,d_train,d_test = importacao('../AquisicaoDados/DataSet/TrainingTestData.json')
#x_train,d_train = importacaoCompleta('../AquisicaoDados/DataSet/TrainingTestData.json')
x_test,d_test = DatasetTest(5)
print(x_test)
print(d_test)
#print(x_train)
#print(d_train)
#for i in range(5):
    #plt.scatter(x_train[i*1000:i*1000 + 1000,0],x_train[i*1000:i*1000 + 1000,1])
#plt.show()
'''
'''
x_train,d_train = importacaoCompleta('../AquisicaoDados/DataSet/TrainingTestData.json')
x_test,d_test = DatasetTest(5)
print(x_test)
print(d_test)
print(x_train)
print(d_train)
'''
Main()