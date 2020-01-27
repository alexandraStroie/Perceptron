import sys
import numpy as np
from numpy import random
from Perceptron import *
import matplotlib.pyplot as plt
import random
from Point import *
import matplotlib.pyplot as plt



p = Perceptron(2)
inputs = [0,0]


# secventa de antrenare
#point = Point(3,4)
panta = 1
for i in range(0,1000000):
    point = Point(random.random(),random.random(),panta)
    #print(point.show_point_label())
    inputs[0] = point.x
    inputs[1] = point.y
    p.training(point.label, 0.1,inputs)



#secventa de test
points_a_x = []
points_a_y= []

points_b_x = []
points_b_y= []

for i in range(0,1000):
    point = Point(random.random(),random.random(),panta)
    #print(point.show_point() +  ' ' + str(p.guess([point.x,point.y])))
    if p.guess([point.x,point.y]) == 1:
        points_a_x.append(point.x)
        points_a_y.append(point.y)
    else:
        points_b_x.append(point.x)
        points_b_y.append(point.y)


plt.plot([0,1/panta],[0,1],'g')
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














