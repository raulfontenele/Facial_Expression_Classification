import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from mpl_toolkits.mplot3d import Axes3D
import random as rand

def line_plot(sensor1,sensor2,gestureName):
    gestureName+=".pdf"
    baseline = plt.plot(sensor1, label='Zigomático')
    baseline = plt.plot(sensor2,  label='Corrugador')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
            ncol=2, mode="expand", borderaxespad=0.)
    plt.show()
    plt.savefig(gestureName, bbox_inches='tight')

def my_ScatterPlot(Matrix):
    rows = list(range(0, len(Matrix)))
    r,c = Matrix.shape
    c-=1
    Count_class = int(np.max(Matrix[:,2]))
    classLoop = list(range(0,int(Count_class)))
    MatrixByClass = [None] * int(Count_class)
    for i in classLoop:
         MatrixByClass[i] = np.array([])
    for i in rows:
        aux1 = Matrix[i,0:2]
        aux = MatrixByClass[int(Matrix[i][2]-1)]
        if aux.size != 0:        
            if aux.size==c:
                aux.shape = (1,c)
            aux1.shape = (1,c)
        
        MatrixByClass[int(Matrix[i][2]-1)] =  np.concatenate((aux,aux1),axis=0)
        
    for i in classLoop:
        print("GESTAO: "+str(i+1)) 
        print(MatrixByClass[i])

    plt.plot(MatrixByClass[0][:,0],MatrixByClass[0][:,1], linestyle='none', marker='o',label='Neutro')
    plt.plot(MatrixByClass[1][:,0],MatrixByClass[1][:,1], linestyle='none', marker='o',label='Sorriso')
    plt.plot(MatrixByClass[2][:,0],MatrixByClass[2][:,1], linestyle='none', marker='o',label='Aberto')
    plt.plot(MatrixByClass[3][:,0],MatrixByClass[3][:,1], linestyle='none', marker='o',label='Surpreso')    
    plt.plot(MatrixByClass[4][:,0],MatrixByClass[4][:,1], linestyle='none', marker='o',label='Grumpy')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
            ncol=2, mode="expand", borderaxespad=0.)
    #plt.show()
    plt.savefig("DataSetTreino5000.pdf", bbox_inches='tight')

def five_subplots(matrixPlot,NameGesture,NameSave,size):
    NameSave+=".png"
    s1 = matrixPlot[0][:,0]
    s2 = matrixPlot[0][:,1]  
    rod = 0
    rodaasas = 4    
    row = [0,1,2]
    column = [0,1]
    fig, axs = plt.subplots(3, 2)
    aux =np.arange(0,0.003*size,0.003)
    #tempo = [0:0.003:0.003]*2999
    for i in row:
        for j in column:
            if(i==2 and j==1):
                break
            if(j==0):
                axs[i,j].set(xlabel='Instante de tempo', ylabel='Amplitude')
            s1 = matrixPlot[rod][:,0]
            s2 = matrixPlot[rod][:,1]
            p1 = axs[i,j].plot(aux,s1,label = "Corr. Supercili")
            p2 = axs[i,j].plot(aux,s2,label= "Zigomático")
            axs[i,j].legend(loc="upper right")
            if(rod<3):
                axs[i,j].get_xaxis().set_visible(False)
            axs[i,j].set_title(NameGesture+' Rodada '+str(rodaasas+1))
            rodaasas+=1
            rod+=1

    
    axs[2,1].set(xlabel='Tempo (s)')    
    #for ax in axs.flat:
        #ax.label_outer()
    fig.subplots_adjust(wspace=0.25)
    fig.delaxes(axs[2,1])
    #plt.show()
    plt.savefig(NameSave, bbox_inches='tight')
    mybp=1


def line_plot_initial(sensor1,sensor2,gestureName):
    gestureName+=".pdf"
    baseline = plt.plot(sensor1, label='Zigomático')
    baseline = plt.plot(sensor2,  label='Corrugador')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
            ncol=2, mode="expand", borderaxespad=0.)
    plt.show()
    plt.savefig(gestureName, bbox_inches='tight')

def stem_plot(sensor1,sensor2,gestureName):
    gestureName+=".pdf"
    markerline, stemlines, baseline = plt.stem(sensor1, markerfmt='o', label='Sensor 1')
    plt.setp(stemlines, 'color', plt.getp(markerline,'color'))
    plt.setp(stemlines, 'linestyle', 'dotted')

    markerline, stemlines, baseline = plt.stem(sensor2, markerfmt='o', label='Sensor 2')
    plt.setp(stemlines, 'color', plt.getp(markerline,'color'))
    plt.setp(stemlines, 'linestyle', 'dotted')

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
            ncol=2, mode="expand", borderaxespad=0.)
    #plt.show()
    plt.savefig(gestureName, bbox_inches='tight')

def TwoD_scatter_plot(t1,t2,t3,t4,t5,rod):
        
    plt.plot(t1[:,0],t1[:,1], linestyle='none', marker='o',label='Neutro')
    plt.plot(t2[:,0],t2[:,1], linestyle='none', marker='o',label='Sorriso')
    plt.plot(t3[:,0],t3[:,1], linestyle='none', marker='o',label='Aberto')
    plt.plot(t4[:,0],t4[:,1], linestyle='none', marker='o',label='Surpreso')    
    plt.plot(t5[:,0],t5[:,1], linestyle='none', marker='o',label='Grumpy')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
            ncol=2, mode="expand", borderaxespad=0.)
    #plt.show()
    plt.savefig("Rodada"+str(rod)+"Scatter2D.pdf", bbox_inches='tight')
    

def TwoD_scatter_plot_fourGesture(t1,t2,t3,t4):
        
    plt.plot(t1[:,0],t1[:,1], linestyle='none', marker='o',label='Classe 1')
    plt.plot(t2[:,0],t2[:,1], linestyle='none', marker='o',label='Classe 2')
    plt.plot(t3[:,0],t3[:,1], linestyle='none', marker='o',label='Classe 3')
    plt.plot(t4[:,0],t4[:,1], linestyle='none', marker='o',label='Classe 4')        
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
            ncol=2, mode="expand", borderaxespad=0.)    
    plt.savefig("Scatter2D_four.pdf", bbox_inches='tight')       



def ThreeD_scatter_plot(allData):
    i = 1
    arr = np.array([])
    while i <= 5:
        auxAr = np.ones((2500))
        auxAr*=i        
        arr = np.concatenate([arr, auxAr])
        
        i += 1
    arr = arr[np.newaxis]
    
    BigMatrix = np.append(allData, arr.T, axis=1)
    
    print("tamanho"+str(np.shape(BigMatrix)))
    fig = plt.figure()
    ax = Axes3D(fig)
    i=0
    int1=0
    int2=3500
    while i<5:
        classes = "Classe "+(str(i+1))
        ax.scatter(BigMatrix[int1:int2,0], BigMatrix[int1:int2,1], BigMatrix[int1:int2,2],label=classes)
        i+=1
        int1+=3500
        int2+=3500
    ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
            ncol=2, mode="expand", borderaxespad=0.)
    ax.set_xlabel('Sensor 1')
    ax.set_ylabel('Sensor 2')
    ax.set_zlabel('Classe')
    plt.savefig("Scatter3D.pdf", bbox_inches='tight') 
    plt.show()
    