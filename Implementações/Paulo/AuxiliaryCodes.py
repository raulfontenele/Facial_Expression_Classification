import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from mpl_toolkits.mplot3d import Axes3D
import random as rand
import json
import requests
import time
import myGraphics
import locale
import csv
def TanHDerivative(x):
    aux = np.power(np.tanh(x), 2)     
    return 1-aux
def BiasGenerator(M):
    aux = np.ones((len(M),1))*-1
    aux.shape = (len(M),1)
    Matrix = np.concatenate((aux,M),axis=1) 
    return Matrix
def GenerateYtrain(M):
    Count_class = int(np.max(M))
    v = [None] * Count_class
    iterator = list(range(0, int(Count_class))) 
    for i in iterator:
        v[i] = np.ones((1,Count_class))*-1
        v[i][0][i] = 1

    BigMatrix = [None] * int(len(M))
    iterator = list(range(0, len(M)))
    for i in iterator:
        BigMatrix[i] = v[int(M[i]-1)]
    
    return BigMatrix
def MinMax(M):
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

def ScrambleData(Matrix):
    #gerando Seed de teino e teste aleatórias.
    RandomSeed = np.random.permutation(5000)
    TrSeed = RandomSeed[0:int((len(RandomSeed)*.8))]
    TeSeed = RandomSeed[int((len(RandomSeed)*.8)):len(RandomSeed)]
    Treino = np.zeros(shape=(len(TrSeed),3))
    Teste = np.zeros(shape=(len(TeSeed),3))
    Matrix.reshape((5000,3))
    pr1 = np.array([])
    pr2 = np.array([])
    rot = np.array([])
    x = list(range(1,len(TrSeed)))

    np.random.shuffle(Matrix)

    for i in TrSeed:
        print(i)


    
       




    return "not ready"
def RetrieveFixedDS():
    Pred1 = np.array([])
    Pred2 = np.array([])
    Rot = np.array([])
    f = open('FixedDS.json')
    data = json.load(f)
    f.close() 

    Ns1 = np.asarray(data['Data']['Pred1'][0])
    Ns1.shape=(len(Ns1),1)
    Ns2 = np.asarray(data['Data']['Pred2'][0])
    Ns2.shape=(len(Ns1),1)
    Ns3 = np.asarray(data['Data']['Classe'][0])
    Ns3.shape=(len(Ns1),1)

    
    M = np.concatenate((Ns1,Ns2,Ns3),axis=1)

    return M
def SaveADS(M):
    f = open('FixedDS.json')
    data = json.load(f)
    f.close()     
    x=np.asarray(M[:,0])
    y=np.asarray(M[:,1])
    z=np.asarray(M[:,2])
    List1  = []
    List2  = []
    List3  = []
    
    for i in range(len(x)):
        List1.append(x[i])
        List2.append(y[i])
        List3.append(z[i])
    
    data['Data']['Pred1'][0] = List1
    data['Data']['Pred2'][0] = List2
    data['Data']['Classe'][0] = List3
    with open('FixedDS.json',"w") as outfile:
        json.dump(data, outfile)

    return 'x'

def RetrieveDataSet(FileName):
    FileName = FileName+".json"
    f = open(FileName)
    data = json.load(f)
    f.close()    
    Pred1 = np.array([])
    Pred2 = np.array([])
    Rot = np.array([])
    #Neutro:
    Ns1 = np.asarray(data['Data']['Neutro'][0])
    Pred1 = np.concatenate((Pred1,Ns1),axis=0)
    #Ns1.shape = (len(Ns1),1)
    Ns2 = np.asarray(data['Data']['Neutro'][1])
    Pred2 = np.concatenate((Pred2,Ns2),axis=0)
    #Ns2.shape = (len(Ns2),1)
    Rotulos = np.ones(len(Ns2))
    Rot = np.concatenate((Rot,Rotulos),axis=0)

    #Sorriso:
    Ns1 = np.asarray(data['Data']['Sorriso'][0])
    Pred1 = np.concatenate((Pred1,Ns1),axis=0)
    #Ns1.shape = (len(Ns1),1)
    Ns2 = np.asarray(data['Data']['Sorriso'][1])
    Pred2 = np.concatenate((Pred2,Ns2),axis=0)                
    #Ns2.shape = (len(Ns2),1)
    Rotulos = np.multiply(np.ones(len(Ns2)),2)       
    Rot = np.concatenate((Rot,Rotulos),axis=0)

    #Aberto:
    Ns1 = np.asarray(data['Data']['Aberto'][0])
    Pred1 = np.concatenate((Pred1,Ns1),axis=0)
    #Ns1.shape = (len(Ns1),1)
    Ns2 = np.asarray(data['Data']['Aberto'][1])
    Pred2 = np.concatenate((Pred2,Ns2),axis=0)
    #Ns2.shape = (len(Ns2),1)
    Rotulos = np.multiply(np.ones(len(Ns2)),3)
    Rot = np.concatenate((Rot,Rotulos),axis=0)

    #Surpreso:
    Ns1 = np.asarray(data['Data']['Surpreso'][0])
    Pred1 = np.concatenate((Pred1,Ns1),axis=0)
    #Ns1.shape = (len(Ns1),1)
    Ns2 = np.asarray(data['Data']['Surpreso'][1])
    Pred2 = np.concatenate((Pred2,Ns2),axis=0)
    #Ns2.shape = (len(Ns2),1)
    Rotulos = np.multiply(np.ones(len(Ns2)),4)
    Rot = np.concatenate((Rot,Rotulos),axis=0)

    #Grumpy:
    Ns1 = np.asarray(data['Data']['Grumpy'][0])
    Pred1 = np.concatenate((Pred1,Ns1),axis=0)

    Pred1.shape = (len(Pred1),1)
    Ns2 = np.asarray(data['Data']['Grumpy'][1])
    Pred2 = np.concatenate((Pred2,Ns2),axis=0)
    Pred2.shape = (len(Pred2),1)
    #Ns2.shape = (len(Ns2),1)

    Rotulos = np.multiply(np.ones(len(Ns2)),5)
    Rot = np.concatenate((Rot,Rotulos),axis=0)
    Rot.shape = (len(Rot),1)
    
    
    Matrix = np.concatenate((Pred1,Pred2,Rot),axis=1)   



    return Matrix


def LastPosition(data,classes):
    Count_class = int(np.max(classes))
    listPosition = [None] * int(Count_class)    
    rowsTr = list(range(0, len(data)))
    for i in rowsTr:
        listPosition[int(classes[i][0])-1] = i     
    
    return listPosition

def InserirRelatorio(parametros):
        for i in range(len(parametros)):            
            parametros[i] = str(parametros[i]).replace(".",",")

        locale.setlocale(locale.LC_ALL, '')
        DELIMITER = ';' if locale.localeconv()['decimal_point'] == ',' else ','
        with open('relatorio.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=DELIMITER)
            writer.writerows([parametros])

def CountClasses(x):
    cl = [0,0,0,0,0]
    
    for k in x:
        if(k==1):
            cl[0]+=1
        elif(k==2):
            cl[1]+=1
        elif(k==3):
            cl[2]+=1
        elif(k==4):
            cl[3]+=1
        else:
            cl[4]+=1
    return cl



def ReturnDataMatrix(SamplesNumber):  
    FileName = "D6V6PADRAO.json"
    f = open(FileName)
    data = json.load(f) 
    f.close()
    iterator = [0,1,2,3,4]
    gestos = ["Neutro","Sorriso","Aberto","Surpreso","Grumpy"]

    
    Sensor1 = []
    Sensor2 = []
    for i in range(5):
        Sensor1.append([])
        Sensor2.append([])
    
    rodadas = list(range(1, 11))
    for x in rodadas:
        randomV = np.random.permutation(1000)
        randomV = randomV[0:SamplesNumber] 

        for j in iterator:
            
            Ns1 = np.asarray(data['Rodada'+str(x)][gestos[j]][0])
            Ns2 = np.asarray(data['Rodada'+str(x)][gestos[j]][1])

            for k in randomV:
                Sensor1[j].append(int(Ns1[k]))
                Sensor2[j].append(int(Ns2[k]))     
            
    f = open('FinalTestDS.json',"r") 
    data1 = json.load(f)
    f.close()    
    for j in iterator:
        data1['Data'][gestos[j]][0] = Sensor1[j]
        data1['Data'][gestos[j]][1] = Sensor2[j]    
    
    with open('FinalTestDS.json',"w") as outfile:
        json.dump(data1, outfile)
    


#Esta função será a oficial de recuperação da matriz de dados:
def RetrieveDataMatrix(FileName="DSV5_padrao"):
    FileName+=".json"
    f = open(FileName) 
    data = json.load(f) 
    f.close()
    ListMatrices = []

    
    rodadas = list(range(1, 11))
    for x in rodadas:
        Pred1 = np.array([])
        Pred2 = np.array([])
        Rot = np.array([])
        #Neutro:
        Ns1 = np.asarray(data['Rodada'+str(x)]['Neutro'][0])
        Pred1 = np.concatenate((Pred1,Ns1),axis=0)
        #Ns1.shape = (len(Ns1),1)
        Ns2 = np.asarray(data['Rodada'+str(x)]['Neutro'][1])
        Pred2 = np.concatenate((Pred2,Ns2),axis=0)
        #Ns2.shape = (len(Ns2),1)
        Rotulos = np.ones(len(Ns2))
        Rot = np.concatenate((Rot,Rotulos),axis=0)

        #Sorriso:
        Ns1 = np.asarray(data['Rodada'+str(x)]['Sorriso'][0])
        Pred1 = np.concatenate((Pred1,Ns1),axis=0)
        #Ns1.shape = (len(Ns1),1)
        Ns2 = np.asarray(data['Rodada'+str(x)]['Sorriso'][1])
        Pred2 = np.concatenate((Pred2,Ns2),axis=0)                
        #Ns2.shape = (len(Ns2),1)
        Rotulos = np.multiply(np.ones(len(Ns2)),2)       
        Rot = np.concatenate((Rot,Rotulos),axis=0)

        #Aberto:
        Ns1 = np.asarray(data['Rodada'+str(x)]['Aberto'][0])
        Pred1 = np.concatenate((Pred1,Ns1),axis=0)
        #Ns1.shape = (len(Ns1),1)
        Ns2 = np.asarray(data['Rodada'+str(x)]['Aberto'][1])
        Pred2 = np.concatenate((Pred2,Ns2),axis=0)
        #Ns2.shape = (len(Ns2),1)
        Rotulos = np.multiply(np.ones(len(Ns2)),3)
        Rot = np.concatenate((Rot,Rotulos),axis=0)

        #Surpreso:
        Ns1 = np.asarray(data['Rodada'+str(x)]['Surpreso'][0])
        Pred1 = np.concatenate((Pred1,Ns1),axis=0)
        #Ns1.shape = (len(Ns1),1)
        Ns2 = np.asarray(data['Rodada'+str(x)]['Surpreso'][1])
        Pred2 = np.concatenate((Pred2,Ns2),axis=0)
        #Ns2.shape = (len(Ns2),1)
        Rotulos = np.multiply(np.ones(len(Ns2)),4)
        Rot = np.concatenate((Rot,Rotulos),axis=0)

        #Grumpy:
        Ns1 = np.asarray(data['Rodada'+str(x)]['Grumpy'][0])
        Pred1 = np.concatenate((Pred1,Ns1),axis=0)

        Pred1.shape = (len(Pred1),1)
        Ns2 = np.asarray(data['Rodada'+str(x)]['Grumpy'][1])
        Pred2 = np.concatenate((Pred2,Ns2),axis=0)
        Pred2.shape = (len(Pred2),1)
        #Ns2.shape = (len(Ns2),1)

        Rotulos = np.multiply(np.ones(len(Ns2)),5)
        Rot = np.concatenate((Rot,Rotulos),axis=0)
        Rot.shape = (len(Rot),1)
        
        
        Matrix = np.concatenate((Pred1,Pred2,Rot),axis=1)     
        ListMatrices.append(Matrix)

    
    return ListMatrices

def CospeJson():

    f = open('ALLDATAControle_NG.json',"r") 
    data = json.load(f) 
    f.close()
    Ns1 = np.asarray(data['Rodada1']['neutro'][0])
    Ns1.shape = (len(Ns1),1)
    Ns2 = np.asarray(data['Rodada1']['neutro'][1])
    Ns2.shape = (len(Ns2),1)
    T1 = np.concatenate((Ns1,Ns2),axis=1)

    Fs1 = np.asarray(data['Rodada1']['feliz'][0])
    Fs1.shape = (len(Fs1),1)
    Fs2 = np.asarray(data['Rodada1']['feliz'][1])
    Fs2.shape = (len(Fs2),1)

    print(T1)



    f = open('testandoJson.json',"r") 
    data = json.load(f) 
    f.close()
    print(data)
    data['Rodada1']['Matriz'] = 0
    
    with open('testandoJson.json',"w") as outfile:
        json.dump(data, outfile)
    
    return "end"
def DadosAq4Padrao():
    f = open('D6V6TRANSICOES.json',"r") 
    data1 = json.load(f) 
    f.close()

    f = open('D6V6PADRAO.json',"r") 
    data = json.load(f) 
    f.close()
    gestos = ['Neutro','Sorriso','Aberto','Surpreso','Grumpy']
    rodadasPadrao = list(range(6, 11)) 
    rodadasTrans = list(range(6, 8)) 

    for j in gestos:
        PlotByGestures = []
        sc1 = np.array([])
        sc2 = np.array([])
        for i in rodadasPadrao:
            Ns1 = np.asarray(data['Rodada'+str(i)][j][0])
            sc1 = np.concatenate((sc1,Ns1))
            Ns1.shape = (len(Ns1),1)
            Ns2 = np.asarray(data['Rodada'+str(i)][j][1])
            sc2 = np.concatenate((sc2,Ns2))
            Ns2.shape = (len(Ns2),1) 
            T4 = np.concatenate((Ns1,Ns2),axis=1) 
            PlotByGestures.append(T4)
        myGraphics.five_subplots(PlotByGestures,j,"Aquisicao4"+j+"Plot"+"LastFive",1000)
            #plt.plot(Ns1,Ns2, linestyle='none', marker='o',label=i)
        #plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
                #ncol=2, mode="expand", borderaxespad=0.)
        #plt.xlabel("Corrugador + Procerus")
        #plt.ylabel("Zigomático + Levator Labili Superiori")        
        #plt.savefig("Aquisicao4Rodada"+str(j)+".png", bbox_inches='tight')       
        #plt.close()

    


    return "fim"

def DadosAq3():
    f = open('Aquisicao_03_padrao.json',"r") 
    data = json.load(f) 
    f.close()
    gestos = ['neutro','feliz','fechado','aberto','Grumpy']
    rodadas =[1,2,3,4,5]    
    
    for j in gestos:
        PlotByGestures = []
        sc1 = np.array([])
        sc2 = np.array([])
        for i in rodadas:            
            Ns1 = np.asarray(data['Rodada'+str(i)][j][0])
            sc1 = np.concatenate((sc1,Ns1))
            Ns1.shape = (len(Ns1),1)
            Ns2 = np.asarray(data['Rodada'+str(i)][j][1])
            sc2 = np.concatenate((sc2,Ns2))
            Ns2.shape = (len(Ns2),1) 
            T4 = np.concatenate((Ns1,Ns2),axis=1) 
            PlotByGestures.append(T4)
        plt.plot(sc1,sc2, linestyle='none', marker='o',label=j)
        
        #myGraphics.five_subplots(PlotByGestures,j,"Aquisicao3"+j+"Plot"+"FirstFive",2500)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
            ncol=2, mode="expand", borderaxespad=0.)
    plt.xlabel("Corrugador Supercílio")
    plt.ylabel("Zigomático")
    plt.savefig("Aquisicao3All_01ScatterPlot.png", bbox_inches='tight')       
    plt.close()
    
    gestos = ['neutro','feliz','fechado','aberto','Surpreso']
    rodadas =[6,7,8,9,10]
    for j in gestos:
        PlotByGestures = []
        sc1 = np.array([])
        sc2 = np.array([])
        for i in rodadas:
            if(j=="feliz"):
                
                Ns1 = np.asarray(data['Rodada'+str(i)][j][0])                
                Ns1.shape = (len(Ns1),1)
                Ns1 = Ns1[0:754,0]
                sc1 = np.concatenate((sc1,Ns1))
                Ns1.shape = (len(Ns1),1)
                Ns2 = np.asarray(data['Rodada'+str(i)][j][1])
                Ns2.shape = (len(Ns2),1)
                Ns2 = Ns2[0:754,0]
                sc2 = np.concatenate((sc2,Ns2))
                Ns2.shape = (len(Ns2),1)

            else:
                Ns1 = np.asarray(data['Rodada'+str(i)][j][0])
                sc1 = np.concatenate((sc1,Ns1))
                Ns1.shape = (len(Ns1),1)
                Ns2 = np.asarray(data['Rodada'+str(i)][j][1])
                sc2 = np.concatenate((sc2,Ns2))
                Ns2.shape = (len(Ns2),1)
            print(j+" Sensor 1 Shape: "+str(Ns1.shape))                                   
            print(j+" Sensor 2 Shape: "+str(Ns2.shape))
            T4 = np.concatenate((Ns1,Ns2),axis=1) 
            PlotByGestures.append(T4)
        plt.plot(sc1,sc2, linestyle='none', marker='o',label=j)
        if(j=="feliz"):
            #myGraphics.five_subplots(PlotByGestures,j,"Aquisicao3"+j+"Plot"+"LastFive",754)
            print("nothing")
        else:
            #myGraphics.five_subplots(PlotByGestures,j,"Aquisicao3"+j+"Plot"+"LastFive",2500)
            print("nothing")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
            ncol=2, mode="expand", borderaxespad=0.)
    plt.xlabel("Corrugador Supercílio")
    plt.ylabel("Zigomático")
    plt.savefig("Aquisicao3_02AllScatterPlot.png", bbox_inches='tight')



    return "a shit"

def GraphToMeeting():
    
    f = open('newData.json',"r") 
    data = json.load(f) 
    f.close()
    #finding the minor array
    gestos = ['neutro','feliz','fechado','aberto']
    for j in gestos:
        print(j)
    rodadas = [2,4,5,6,7,8]
    
    arr_neutro_s1 = np.empty(((2500*6),1), int)
    arr_neutro_s2 = np.array([])
    print(arr_neutro_s1.shape)


    arr_feliz_s1 = np.empty(((2500*6),1), int)
    arr_feliz_s2 = np.empty(((2500*6),1), int)

    arr_aberto_s1 = np.empty(((2500*6),1), int)
    arr_aberto_s2 = np.empty(((2500*6),1), int)

    arr_fechado_s1 = np.empty(((2500*6),1), int)
    arr_fechado_s2 = np.empty(((2500*6),1), int)
    

    for i in rodadas:               

        Ns1 = np.asarray(data['Rodada'+str(i)]['neutro'][0])
        Ns1.shape = (len(Ns1),1)
        Ns2 = np.asarray(data['Rodada'+str(i)]['neutro'][1])
        Ns2.shape = (len(Ns2),1)  

        arr_neutro_s2 = np.concatenate((arr_neutro_s2,Ns2),axis=0)     

        Fs1 = np.asarray(data['Rodada'+str(i)]['feliz'][0])
        Fs1.shape = (len(Fs1),1)
        Fs2 = np.asarray(data['Rodada'+str(i)]['feliz'][1])
        Fs2.shape = (len(Fs2),1)
        


        FEs1 = np.asarray(data['Rodada'+str(i)]['fechado'][0])
        FEs1.shape = (len(FEs1),1)
        FEs2 = np.asarray(data['Rodada'+str(i)]['fechado'][1])
        FEs2.shape = (len(FEs2),1)
        

        As1 = np.asarray(data['Rodada'+str(i)]['aberto'][0])
        As1.shape = (len(As1),1)
        As2 = np.asarray(data['Rodada'+str(i)]['aberto'][1])
        As2.shape = (len(As2),1)




    i = 1
    while i <= 10:
        
        i+=1

    return "fim"

def CheckArraysSize():
    f = open('DSV5.json',"r") 
    data = json.load(f)
    f.close()
    ids = list(range(7, 57))
    aux = 0
    rodada = 1
    for x in ids:
        if aux%5==0:
            print("==================================")
            print("Rodada "+str(rodada))            
            print("==================================")

        stringId = 'http://192.168.0.17/webapp/tcc/public/api/info/'+str(x)+'/retrieve'
        response = requests.get(stringId)  
        gesto = response.json()['gesture3']
        print(gesto)
        Ns1 = np.asarray(response.json()['sensor1']) 
        l1=response.json()['sensor1']
        l2=[]

        for i in range(len(l1)):
            t = int(l1[i])
            l2.append(t)

        auxS1 = l2

        data['Rodada'+str(rodada)][gesto][0] = l2
        print('Size S1:'+str(len(Ns1)))

        Ns2 = np.asarray(response.json()['sensor2'])
        l1=response.json()['sensor2']
        l2=[]

        for i in range(len(l1)):
            t = int(l1[i])
            l2.append(t)
      
        auxS2 = l2

        data['Rodada'+str(rodada)][gesto][1] = l2
        print('Size S2:'+str(len(Ns2)))

        if (len(Ns1)!=1000 or len(Ns2)!=1000):
            print("ERRO NOS TAMANHOS NO GESTO "+gesto+" e rodada"+str(rodada))
        elif(x<12):
            myGraphics.line_plot(auxS1,auxS2,"Teste"+gesto)


        
            
        time.sleep(4)
        aux+=1
        if aux%5==0:
            rodada+=1
        

    
    with open('DSV5.json',"w") as outfile:
        json.dump(data, outfile)
    
 
    return "end"

def JsonToNumpy(rodada):
    
    f = open('newData.json',"r") 
    data = json.load(f) 
    f.close()
    Ns1 = np.asarray(data['Rodada'+str(rodada)]['neutro'][0])
    Ns1.shape = (len(Ns1),1)
    Ns2 = np.asarray(data['Rodada'+str(rodada)]['neutro'][1])
    Ns2.shape = (len(Ns2),1)
    T1 = np.concatenate((Ns1,Ns2),axis=1)

    Fs1 = np.asarray(data['Rodada'+str(rodada)]['feliz'][0])
    Fs1.shape = (len(Fs1),1)
    Fs2 = np.asarray(data['Rodada'+str(rodada)]['feliz'][1])
    Fs2.shape = (len(Fs2),1)
    T2 = np.concatenate((Fs1,Fs2),axis=1)


    FEs1 = np.asarray(data['Rodada'+str(rodada)]['fechado'][0])
    FEs1.shape = (len(FEs1),1)
    FEs2 = np.asarray(data['Rodada'+str(rodada)]['fechado'][1])
    FEs2.shape = (len(FEs2),1)
    T3 = np.concatenate((FEs1,FEs2),axis=1)

    As1 = np.asarray(data['Rodada'+str(rodada)]['aberto'][0])
    As1.shape = (len(As1),1)
    As2 = np.asarray(data['Rodada'+str(rodada)]['aberto'][1])
    As2.shape = (len(As2),1)
    T4 = np.concatenate((As1,As2),axis=1)    

    return T1,T2,T3,T4

def RetrieveMatrixData_four():
    return "finished"

def RetrieveMatrixData_five():
    f = open('cinc_gesture_controle.json',"r")     
    data = json.load(f)
    f.close()
    rodada = 'Rodada'

    

    return "finished"

def JsonToNumpy_five(rod):
    
    f = open('D6V6PADRAO.json',"r") 
    rodada = 'Rodada'+str(rod)
    data = json.load(f) 
    f.close()
    Ns1 = np.asarray(data[rodada]['Neutro'][0])
    Ns1.shape = (len(Ns1),1)
    Ns2 = np.asarray(data[rodada]['Neutro'][1])
    Ns2.shape = (len(Ns2),1)
    T1 = np.concatenate((Ns1,Ns2),axis=1)

    Fs1 = np.asarray(data[rodada]['Sorriso'][0])
    Fs1.shape = (len(Fs1),1)
    Fs2 = np.asarray(data[rodada]['Sorriso'][1])
    Fs2.shape = (len(Fs2),1)
    T2 = np.concatenate((Fs1,Fs2),axis=1)


    FEs1 = np.asarray(data[rodada]['Aberto'][0])
    FEs1.shape = (len(FEs1),1)
    FEs2 = np.asarray(data[rodada]['Aberto'][1])
    FEs2.shape = (len(FEs2),1)
    T3 = np.concatenate((FEs1,FEs2),axis=1)

    As1 = np.asarray(data[rodada]['Surpreso'][0])
    As1.shape = (len(As1),1)
    As2 = np.asarray(data[rodada]['Surpreso'][1])
    As2.shape = (len(As2),1)
    T4 = np.concatenate((As1,As2),axis=1)

    Gs1 = np.asarray(data[rodada]['Grumpy'][0])
    Gs1.shape = (len(Gs1),1)
    Gs2 = np.asarray(data[rodada]['Grumpy'][1])
    Gs2.shape = (len(Gs2),1)
    T5 = np.concatenate((Gs1,Gs2),axis=1)

 
     

    return T1,T2,T3,T4,T5

def MuksMaks():
    
    f = open('ALLDATAControle_NG.json',"r") 
    data = json.load(f) 
    f.close()
    Ns1 = np.asarray(data['Rodada2']['neutro'][0])
    Ns1.shape = (len(Ns1),1)
    Ns2 = np.asarray(data['Rodada2']['neutro'][1])
    Ns2.shape = (len(Ns2),1)
    T1 = np.concatenate((Ns1,Ns2),axis=1)

    Fs1 = np.asarray(data['Rodada2']['feliz'][0])
    Fs1.shape = (len(Fs1),1)
    Fs2 = np.asarray(data['Rodada2']['feliz'][1])
    Fs2.shape = (len(Fs2),1)
    T2 = np.concatenate((Fs1,Fs2),axis=1)


    FEs1 = np.asarray(data['Rodada2']['fechado'][0])
    FEs1.shape = (len(FEs1),1)
    FEs2 = np.asarray(data['Rodada2']['fechado'][1])
    FEs2.shape = (len(FEs2),1)
    T3 = np.concatenate((FEs1,FEs2),axis=1)

    As1 = np.asarray(data['Rodada2']['aberto'][0])
    As1.shape = (len(As1),1)
    As2 = np.asarray(data['Rodada2']['aberto'][1])
    As2.shape = (len(As2),1)
    T4 = np.concatenate((As1,As2),axis=1)

    Gs1 = np.asarray(data['Rodada2']['Grumpy'][0])
    Gs1.shape = (len(Gs1),1)
    Gs2 = np.asarray(data['Rodada2']['Grumpy'][1])
    Gs2.shape = (len(Gs2),1)
    T5 = np.concatenate((Gs1,Gs2),axis=1)

 
     

    return T1,T2,T3,T4,T5





def FirstDataSet():
    
    f = open('dataTrab_NG.json',"r") 
    data = json.load(f) 
    f.close()
    Ns1 = np.asarray(data['DATA_MATRIX']['neutro'][0])
    Ns1.shape = (len(Ns1),1)
    Ns2 = np.asarray(data['DATA_MATRIX']['neutro'][1])
    Ns2.shape = (len(Ns2),1)
    T1 = np.concatenate((Ns1,Ns2),axis=1)

    Fs1 = np.asarray(data['DATA_MATRIX']['feliz'][0])
    Fs1.shape = (len(Fs1),1)
    Fs2 = np.asarray(data['DATA_MATRIX']['feliz'][1])
    Fs2.shape = (len(Fs2),1)
    T2 = np.concatenate((Fs1,Fs2),axis=1)


    FEs1 = np.asarray(data['DATA_MATRIX']['fechado'][0])
    FEs1.shape = (len(FEs1),1)
    FEs2 = np.asarray(data['DATA_MATRIX']['fechado'][1])
    FEs2.shape = (len(FEs2),1)
    T3 = np.concatenate((FEs1,FEs2),axis=1)

    As1 = np.asarray(data['DATA_MATRIX']['aberto'][0])
    As1.shape = (len(As1),1)
    As2 = np.asarray(data['DATA_MATRIX']['aberto'][1])
    As2.shape = (len(As2),1)
    T4 = np.concatenate((As1,As2),axis=1)

    Gs1 = np.asarray(data['DATA_MATRIX']['grumpy'][0])
    Gs1.shape = (len(Gs1),1)
    Gs2 = np.asarray(data['DATA_MATRIX']['grumpy'][1])
    Gs2.shape = (len(Gs2),1)
    T5 = np.concatenate((Gs1,Gs2),axis=1)

 
     

    return T1,T2,T3,T4,T5
 

