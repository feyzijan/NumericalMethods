#-------------------------------------------------------------------------------
# Name:        module4
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
# Task a: Write a function that receives a matrix and returns its trace
# Trace of a matrix: Sum of Components in its main diagonal



A = [[1,2,3,4],[5,6,7,8,9],[10,11,12,13],[14,15,16,17]]


def Trace(A):
    n = len(A)
    if len(A) != len(A[0]):
        return 0
    Rn = range(0,n)
    t= 0
    for i in Rn:
        t += A[i][i]
    return t

print(Trace(A))