#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Feyzi Can Eser
#
# Created:     18.04.2020
# Copyright:   (c) Feyzi Can Eser 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import math as mat
import matplotlib.pyplot as plt
#import numpy as np

#Distances (m)
L = 10
D = 2

#Angle (radians) and speed (m/s)
o = (mat.pi)/(3)
v = 2

#print(mat.cos(o))



t = L/(v*mat.cos(o))



print('Time taken: ' + str(t))

n = ((t - (D/2/v/mat.sin(o))) * v * mat.sin(o)/D) +1

#print(n)

ne = mat.floor(n)
print('The ball bounces ' + str(ne) + ' times')


#Now plot trajectory

#Decide on dx and dy
dt = 0.01

#store all x and y positions within a given change in time in a list
X = []
Y = []


l = int(t/dt) + 1


for i in range(0,int(l)):
    X = X + [i*v*mat.cos(o)*dt]






#Y position list
y = 0
u = 1
for i in range(0,l):
    y = y + u*v*mat.sin(o)*dt
    if (-D <= y <= D):
        Y = Y + [y]
    if (y > D):
        y = 2 - (y-2)
        u = -1
        Y = Y + [y]
    if (y < -D):
        y = -2 + (-2-y)
        u = 1
        Y = Y + [y]



#Check plot
plt.axis([0,L,-D,D])
plt.plot(X,Y)










