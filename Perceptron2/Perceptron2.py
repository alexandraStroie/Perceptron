import sys
import numpy as np
from numpy import *
import random
from Point2 import *


#activation function 
def sign(n):
    if(n>=0):
        return 1
    else:
        return -1



class Perceptron2:
    
    weights = []

    def __init__(self,size):
        for i in range(0,size):
            #weights[i] = random.randint(-1,1)
            self.weights.append(0)
            
                       
                    
    def guess(self, inputs):
        sum_input_weights = 0
        #print(len(inputs))
        for i in range(0, len(inputs)):
            sum_input_weights = sum_input_weights + inputs[i] * self.weights[i]
        output_s = sign(sum_input_weights)       
        return output_s
    
    
    #lr = learning rate
    def training(self, label, lr, inputs):
        err = label - self.guess(inputs)
        for i in range(0,len(inputs)):
            self.weights[i] = self.weights[i] + lr * err * inputs[i]

    