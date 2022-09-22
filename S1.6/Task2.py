#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      feyzi
#
# Created:     11/01/2020
# Copyright:   (c) feyzi 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import matplotlib.pyplot as pl
import math as mt

def Factorial(a):
    Rn =range(0,a)
    af = 1
    for i in Rn:
        af = af * (a-i)
    return af


a = 0
dx = 0.01
b = 5
L = [a,dx,b]




def ExpSeries(L):
    RN = range(18,19)
    #i.e. for ranges 2,6,10,14

    for N in RN:

        Ri = range(0,N+1)
        #set range of i based on current N value

        x =[]
        y =[]

        #initialise the lists storing x and y

        xp = L[0]

        #give the starting value of x

        while (xp <= L[2]):
            yp = 0  #initialise the sum

            for i in Ri:
                yp = yp + ((xp)**i)/(Factorial(i))

            #store current x and y values

            x = x + [xp]
            y = y + [yp]
            if (xp > 4.799 and xp < 4.801 ):
                print(yp)

            xp = xp + L[1]  #increase the value of x by dx

        #print(y)
    return(x,y)



pl.plot(ExpSeries(L)[0],ExpSeries(L)[1])
pl.xlabel('x axis')
pl.ylabel('y axis')
pl.title('e to the power of x')
pl.show

for val in ExpSeries(L)[0]:
            yex = mt.exp(val)
            pl.scatter(val, yex)




