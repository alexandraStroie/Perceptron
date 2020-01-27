import sys
import numpy as np
from numpy import random
from Perceptron2 import *
import matplotlib.pyplot as plt
import random
from Point2 import *
import matplotlib.pyplot as plt

    
p = Perceptron2(3)    
inputs = [0,0,1]

print(len(inputs))
    
# secventa de antrenare     
#point = Point(3,4)
panta = 0.7
#m=bias
m=0.5
for i in range(0,10000):
    point = Point2(random.random(),random.random(),panta,m)
    #print(point.show_point_label())
    inputs[0] = point.x
    inputs[1] = point.y
    inputs[2] = 1
    p.training(point.label, 0.3,inputs)



#secventa de test
points_a_x = []
points_a_y= []

points_b_x = []
points_b_y= []
 
for i in range(0,10000):
    point = Point2(random.random(),random.random(),panta,m)
    #print(point.show_point() +  ' ' + str(p.guess([point.x,point.y]))) 
    if p.guess([point.x,point.y,1]) == 1:
        points_a_x.append(point.x)
        points_a_y.append(point.y)
    else:
        points_b_x.append(point.x)
        points_b_y.append(point.y)   
    
   

plt.plot([0,(1-m)/panta],[m,1],'g')     
plt.scatter(points_a_x, points_a_y, color='red')
plt.scatter(points_b_x, points_b_y, color='blue')
plt.show()
      
    
  
  
# N1 = 7
# N2 = 7
# x1 = np.random.rand(N1)
# y1 = np.random.rand(N1)
# x2 = np.random.rand(N2)
# y2 = np.random.rand(N2)
# plt.scatter(x1, y1, color='red')
# plt.scatter(x2, y2, color='blue')
# plt.show()


# point1 = Point(0,1,3)
# point2 = Point(0.3,5,3)
# 
# plt.plot([0,2],[1,5])     
# plt.show() 
#      

     


     
 
     
     
     
     
     
     
     
     
     
     
     