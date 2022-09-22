#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Feyzi Can Eser
#
# Created:     20.04.2020
# Copyright:   (c) Feyzi Can Eser 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()



import random as rn
import matplotlib.pyplot as plt
import math as mat


# Brick of Length 0.2 within a 2x2 square
# generate random position and the required shooting angles



xp = rn.uniform(0.1,2)
yp = rn.uniform(0,2)
print('center is at x: ' + str(xp) + ' y: ' + str(yp))

xs = xp - 0.1
xe = xp + 0.1

omin = mat.atan(yp/xs)
omax = mat.atan(yp/xe)

omind = round((omin / mat.pi*180), 2)
omaxd = round ((omax / mat.pi*180), 2)

print('Minimum possible shooting angle is ' + str(omind) + ' degrees')
print('Maximium possible shooting angle is ' + str(omaxd) + ' degrees')


Lx= []
Ly = []


for i in range(0,201):
    Lx += [xs + i/1000]

for i in range(0,201):
    Ly += [yp]





LPx = []
LPy = []

hit = False


for i in range(0,200):
        xx = i/100*mat.cos((omax+omin)/2)
        yy = i/100*mat.sin((omax+omin)/2)
        if ( yy < yp):
            LPx += [xx]
            LPy += [yy]




plt.axis([0, 2, 0, 2])
plt.plot(Lx,Ly)

plt.plot(LPx,LPy)



