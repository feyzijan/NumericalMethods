#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      fce19
#
# Created:     06/03/2020
# Copyright:   (c) fce19 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import matplotlib.pyplot as plt

#Task E: Read maps and find the treasure ;p

f = open('Map1.txt', 'r')
a = f.readlines()
m = int(a[0])
n = int(a[1])
Rm = range(0,m)
Rn = range(0,n)

a.pop(0)
a.pop(0)

A = []

for item in a:
    A += [int(item)]


#Turn list into Matrix
def ListToMatrix(A,m,n):
    Rrow = range(0,m)
    Am = []
    for i in Rrow:
        t = []
        R = range (n*(i-1),n*i)
        for j in R:
            t += [A[j]]
        Am += [t]
    return Am


P = ListToMatrix(A,m,n)
for row in P:
    print(row)


#Need to convert this into a map


