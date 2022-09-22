#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      fce19
#
# Created:     07/02/2020
# Copyright:   (c) fce19 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


 #Task 2: Define Matrices

A =[[24,67,81],[0,3,28],[63,55,17]]

#for row in A:
   # print(row)

A[0][1],A[2][2] = A[2][2], A[0][1]

A[0][2], A[2][0] = A[2][0], A[0][2]

A[1][1] = A[0][0] + A[1][2]

for row in A:
    print(row)


B = [[3,5,7],[2,4,6]]



