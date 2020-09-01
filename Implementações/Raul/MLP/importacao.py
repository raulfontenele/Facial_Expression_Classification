import pandas as pd

def converterClasses(diretorio):
    linhas = open(diretorio,'r').readlines()
    print(linhas)
    arq_escrita = open(diretorio,'w')
    for linha in linhas:
        if int(linha) == 1:
            arq_escrita.write("-1,-1,1" + '\n')
        elif int(linha) == 2:
            arq_escrita.write("-1,1,-1"+ '\n')
        else:
            arq_escrita.write("1,-1,-1"+ '\n')
    arq_escrita.close()
    
    return 

def converterClasses_1(diretorio):
    linhas = open(diretorio,'r').readlines()
    print(linhas)
    arq_escrita = open(diretorio,'w')
    for linha in linhas:
        if int(linha) == 1:
            arq_escrita.write("-1,1" + '\n')
        elif int(linha) == 2:
            arq_escrita.write("1,-1"+ '\n')
        else:
            arq_escrita.write("1,1"+ '\n')
    arq_escrita.close()
    
    return 

def Main():
    x_train = pd.read_csv('Dataset/xtrain_3spirals.txt',sep='	', header = None)
    x_test = pd.read_csv('Dataset/xtrain_3spirals.txt',sep='	', header = None)

    #converterClasses('Dataset/dtest_3spirals.txt')
    #converterClasses('Dataset/dtrain_3spirals.txt')

    d_train = pd.read_csv('Dataset/dtrain_3spirals.txt',sep=',', header = None)
    d_test = pd.read_csv('Dataset/dtest_3spirals.txt',sep=',', header = None)

#Main()


converterClasses('Dataset/dtest_3spirals.txt')
converterClasses('Dataset/dtrain_3spirals.txt')

#converterClasses_1("Dataset/dtrain_3spirals.txt")
#converterClasses_1("Dataset/dtest_3spirals.txt")
