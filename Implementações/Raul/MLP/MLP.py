import numpy as np
import math
import matplotlib. pyplot as plt
from datetime import datetime

class MLP():
    def __init__(self,n_epoch,learn_rate,precision,hidden_layers,margin = 1000):
        self.n_epoch = n_epoch
        self.learn_rate = learn_rate
        self.precision = precision
        self.hidden_layers = hidden_layers
        self.weights = []
        self.limits = []
        self.margin = margin

    def train(self,x_train,d_train):
        #Inicialização de variáveis da rede neural
        I,Y,gradient,self.weights,accumulator = self.init_variables(len(x_train[0,:]),len(d_train[0,:]))
        x_train = self.preparateInputData(x_train,self.margin,'train')
        eqm = [0, self.precision+1]
        epoch = 0
        histEqm = []

        while True:

            eqm[0] = eqm[1]
            squareError = 0

            #Zerar o acumulador
            for index in range(len(accumulator)):
                accumulator[index] = np.zeros((len(accumulator[index]),len(accumulator[index][0,:])))
            
            for sample in range( len(x_train) ):
                # Foward
                for ctr in range( len(self.hidden_layers) + 1 ):
                    if ctr == 0:
                        I[ctr] = np.dot(self.weights[ctr] , x_train[sample,:][np.newaxis].transpose())
                        Y[ctr] = np.concatenate( (-1*np.ones((1,1)), np.tanh(I[ctr])) )
                    elif ctr == len(self.hidden_layers):
                        I[ctr] = np.dot(self.weights[ctr],Y[ctr-1])
                        Y[ctr] = np.tanh(I[ctr])
                    else:
                        I[ctr] = np.dot(self.weights[ctr],Y[ctr-1])
                        Y[ctr] = np.concatenate( (-1*np.ones((1,1)), np.tanh(I[ctr])) )

                #Backward
                for ctr in reversed( range( len(self.hidden_layers) + 1 ) ):
                    if ctr == 0:
                        gradient[ctr] = np.dot(self.weights[ctr+1][:,1::].transpose(),gradient[ctr + 1]) * self.diff_tanh(I[ctr]) 
                        accumulator[ctr] += self.learn_rate * np.dot(gradient[ctr],x_train[sample,:][np.newaxis])
                    elif ctr == len(self.hidden_layers):
                        gradient[ctr] = (d_train[sample,:][np.newaxis].transpose() - Y[ctr]) * self.diff_tanh(I[ctr])
                        accumulator[ctr] += self.learn_rate * (gradient[ctr]@Y[ctr-1].transpose())
                    else:
                        gradient[ctr] = np.dot(self.weights[ctr+1][:,1::].transpose() , gradient[ctr + 1]) * self.diff_tanh(I[ctr])
                        accumulator[ctr] += self.learn_rate * np.dot(gradient[ctr],Y[ctr - 1].transpose())

            # Ajuste dos pesos da rede neural
            for ctr in range(len(self.hidden_layers) + 1):
                self.weights[ctr] += accumulator[ctr] / len(x_train)

            #Forward para cálculo do erro
            for sample in range( len(x_train) ):
                # Foward
                for ctr in range( len(self.hidden_layers) + 1 ):
                    if ctr == 0:
                        I[ctr] = np.dot(self.weights[ctr],x_train[sample,:][np.newaxis].transpose()) 
                        Y[ctr] = np.concatenate( (-1*np.ones((1,1)), np.tanh(I[ctr])) )
                    elif ctr == len(self.hidden_layers):
                        I[ctr] = np.dot(self.weights[ctr],Y[ctr-1])
                        Y[ctr] = np.tanh(I[ctr])
                    else:
                        I[ctr] = np.dot(self.weights[ctr],Y[ctr-1])
                        Y[ctr] = np.concatenate( (-1*np.ones((1,1)), np.tanh(I[ctr])) )

                squareError += sum(( d_train[sample,:][np.newaxis].transpose() - Y[len(self.hidden_layers)] )**2)
            
            eqm[1] = squareError/len(x_train)
            histEqm.append(eqm[1])

            if(abs(eqm[1] - eqm[0])<=self.precision or epoch>self.n_epoch):
                return [epoch,histEqm]

            epoch+=1


    def application(self,x_app):
        #Inicialização de variáveis
        variables = self.init_variables(len(self.weights[0][0,:]),len(self.weights[len(self.hidden_layers)]))
        I = variables[0]
        Y = variables[1]

        result = []

        #Normalização dos dados de entrada
        x_app = self.preparateInputData(x_app,self.margin,'app')

        for sample in range( len(x_app) ):
            # Foward
            for ctr in range( len(self.hidden_layers) + 1 ):
                if ctr == 0:
                    I[ctr] = np.dot(self.weights[ctr],x_app[sample,:][np.newaxis].transpose()) 
                    Y[ctr] = np.concatenate( (-1*np.ones((1,1)), np.tanh(I[ctr])) )
                elif ctr == len(self.hidden_layers):
                    I[ctr] = np.dot(self.weights[ctr],Y[ctr-1])
                    Y[ctr] = np.tanh(I[ctr])
                else:
                    I[ctr] = np.dot(self.weights[ctr],Y[ctr-1])
                    Y[ctr] = np.concatenate( (-1*np.ones((1,1)), np.tanh(I[ctr])) )

            result.append(self.realizeProbability(Y[len(self.hidden_layers)]))
        
        return result

    def init_variables(self,x_train_length,d_train_length):
        weights = []
        I = []
        Y = []
        accumulator = []
        gradient = []

        # Inicializar as entradas e saídas de cada camada e o gradiente ( que possui as mesmas dimenssões da entrada da camada)
        for index in range(len(self.hidden_layers) +1):
            if index == len(self.hidden_layers):
                Iaux = np.zeros((d_train_length,1))
                Yaux = np.zeros((d_train_length,1))
            else:
                Iaux = np.zeros((self.hidden_layers[index],1))
                Yaux = np.zeros((self.hidden_layers[index]+1,1))

            I.append(Iaux)
            Y.append(Yaux)
            gradient.append(Iaux)

        # Inicializar as matrizes de pesos e o acumulador
        for index in range(len(self.hidden_layers)+1):
            if index == 0:
                weight = np.random.rand(self.hidden_layers[index], x_train_length+1)-0.5
                acc = np.zeros((self.hidden_layers[index], x_train_length+1))
            elif index == len(self.hidden_layers):
                weight = np.random.rand(d_train_length,self.hidden_layers[index-1] + 1)-0.5
                acc = np.zeros((d_train_length,self.hidden_layers[index-1] +1))
            else:
                weight = np.random.rand(self.hidden_layers[index], self.hidden_layers[index-1]+1)-0.5
                acc = np.zeros((self.hidden_layers[index], self.hidden_layers[index-1]+1))
            
            weights.append(weight)
            accumulator.append(acc)

        return I,Y,gradient,weights,accumulator
            
    def realizeProbability(self, vector):
        result = []
        for index in range(len(vector)):
            if vector[index] == max(vector):
                result.append(1)
            else:
                result.append(-1)
        
        return result

    def diff_tanh(self,value):
        return (1 - np.tanh(value)**2)
    
    def preparateInputData(self, inputData, margin,application):
        #Normalização dos dados e guardar os maiores e menores valores por coluna
        new_inputData = self.normalizeData(inputData,margin,application)

        #Concatenar uma matriz coluna igual a -1
        aux_matrix = -1 * np.ones( (len(new_inputData),1) )
        new_inputData = np.concatenate((aux_matrix,new_inputData),axis=1)

        return new_inputData
    
    def normalizeData(self,inputData,margin,application):

        if application == 'train':
            #Normalização dos dados e guardar os maiores e menores valores por coluna
            for column in range(len(inputData[0])):
                self.limits.append([ max(inputData[:,column]), min(inputData[:,column] )])
                inputData[:,column] = (( inputData[:,column] - (min(inputData[:,column])-margin) ) / ( max(inputData[:,column]) - min(inputData[:,column]) + 2*margin)) -0.5
        else:
            #Normalização dos dados e guardar os maiores e menores valores por coluna
            for column in range(len(inputData[0])):
                inputData[:,column] = ( inputData[:,column] - (self.limits[column][1]-margin) ) / ( self.limits[column][0] - self.limits[column][1] + 2*margin) -0.5

        return inputData
