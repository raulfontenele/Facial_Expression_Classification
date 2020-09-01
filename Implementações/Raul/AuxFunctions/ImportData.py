import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def importacao(caminho):
    dataset_json = pd.read_json(caminho).to_numpy()
    dataset = pd.DataFrame()

    ## Inicializar classes 
    classes = np.zeros([5000,5])
    sample_cl = [[1,-1,-1,-1,-1],[-1,1,-1,-1,-1],[-1,-1,1,-1,-1],[-1,-1,-1,1,-1],[-1,-1,-1,-1,1]]
    for exp in range(5):
            data  = exp*1000
            classes[data:data+1000,:] = sample_cl[exp]
    classes = pd.DataFrame(classes)

    ## Organizar dataset
    for exp in dataset_json:
        aux = pd.DataFrame([exp[0][0],exp[0][1]]).T
        dataset = pd.concat([dataset,aux])

    x_train,x_test,d_train,d_test = train_test_split(dataset,classes,test_size = 0.2)

    '''
    d_train = d_train.to_numpy()
    sample_cl = np.array(sample_cl)

    ## Verificar a proporção de cada uma das classes.
    count = [0,0,0,0,0]
    for row in d_train:
        for ind in range(5):
            if np.array_equal(row,sample_cl[ind]):
                count[ind]+=1
                break
    print(count)
    '''
    ## Salvar variáveis em um csv
    x_train.to_csv("x_train.csv")
    d_train.to_csv("d_train.csv")
    x_test.to_csv("x_test.csv")
    d_test.to_csv("d_test.csv")

    return [x_train.to_numpy().astype(np.float64),x_test.to_numpy().astype(np.float64),d_train.to_numpy().astype(np.float64),d_test.to_numpy().astype(np.float64)]

def importacaoCompleta(caminho):
    dataset_json = pd.read_json(caminho).to_numpy()
    dataset = pd.DataFrame()
    ## Inicializar classes 
    classes = np.zeros([5000,5])
    sample_cl = [[-1,-1,1,-1,-1],[-1,-1,-1,-1,1],[1,-1,-1,-1,-1],[-1,1,-1,-1,-1],[-1,-1,-1,1,-1]]
    for exp in range(5):
            data  = exp*1000
            classes[data:data+1000,:] = sample_cl[exp]
    classes = pd.DataFrame(classes)

    ## Organizar dataset
    for exp in dataset_json:
        aux = pd.DataFrame([exp[0][0],exp[0][1]]).T
        dataset = pd.concat([dataset,aux])

    return [dataset.to_numpy().astype(np.float64),classes.to_numpy().astype(np.float64)]