import random
#from matplotlib.patheffects import Stroke
#from matplotlib.pyplot import fill
import matplotlib.pyplot as mat
import matplotlib.patheffects as eff
#import matplotlib.patches as eli
from sympy import ellipse
import matplotlib.pyplot as plt



class Point2:
    def __init__(self,x,y,panta, m):
        self.x = x
        self.y = y
        self.panta = panta
        self.m = m
        y_dr = panta * self.x + self.m
        
        
        if self.y > y_dr:
            self.label = 1
        else:
            self.label = -1    
    
    
    
    def show_point(self):   
        return  str(self.x) + ' ' + str(self.y)
   
            
     
    def show_point_label(self):
        return self.show_point() + ' ' + str(self.label)      


    def line(self):
        return (0.3* self.x + 0.2)      
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                