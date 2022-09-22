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

    import math as mat
    import matplotlib.pyplot as pyplot


    # Using readlines()

    f = open('xaxis.txt', 'r')
    a = f.readlines()

    a = [x.strip() for x in a]

    X = []
    for i in range(0,len(a)):
        X +=  [float(a[i])]



#len A = 400
    r = X[len(X)-1] - X[0]
    print(r)




    Y = [] #Y list

    R = range(0,len(X))

    for i in R:
        y = 0
        for n in range(0,11):
            y = y + ((-1)**(n)) * ((X[i])**(2*n)) / mat.factorial(((2*n)+1))
        Y +=[y]


    DY = [] #derivative list

    for i in range(1,len(X)-1):
        dy = (Y[i+1] - Y[i-1])/(X[i+1]-X[i-1])
        DY += [dy]

    pyplot.scatter(X,Y)

    X.pop(0)
    X.pop(len(X)-1)


    pyplot.scatter(X,DY)










