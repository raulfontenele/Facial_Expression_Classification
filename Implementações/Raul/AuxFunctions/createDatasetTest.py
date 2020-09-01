import numpy as np
import json

def DatasetTest(SamplesNumber):  
    FileName = "../AquisicaoDados/Aquisicao_06/Aquisicao_06_padrao.json"
    f = open(FileName)
    data = json.load(f) 
    f.close()
    iterator = [0,1,2,3,4]
    gestos = ["Neutro","Sorriso","Aberto","Surpreso","Grumpy"]

    ## Inicializar classes 
    classes = np.zeros([5000,5])
    sample_cl = [[1,-1,-1,-1,-1],[-1,1,-1,-1,-1],[-1,-1,1,-1,-1],[-1,-1,-1,1,-1],[-1,-1,-1,-1,1]]
    for exp in range(5):
            dt  = exp*1000
            classes[dt:dt+1000,:] = sample_cl[exp]  
    
    x_test = np.zeros((SamplesNumber*5*10,2))
    d_test = np.zeros((SamplesNumber*5*10,5))

    rodadas = list(range(1, 11))
    for x in rodadas:
        randomV = np.random.permutation(1000)
        randomV = randomV[0:SamplesNumber] 

        for j in iterator:
            
            Ns1 = np.asarray(data['Rodada'+str(x)][gestos[j]][0])
            Ns2 = np.asarray(data['Rodada'+str(x)][gestos[j]][1])
            aux = 0
            for k in randomV:
                x_test[aux + j*SamplesNumber + (x - 1)*SamplesNumber*5][0] = float(Ns1[k])
                x_test[aux + j*SamplesNumber + (x - 1)*SamplesNumber*5][1] = float(Ns2[k])
                d_test[aux + j*SamplesNumber + (x - 1)*SamplesNumber*5][:] = classes[j*1000 + k][:]
                aux +=1

    return x_test,d_test
