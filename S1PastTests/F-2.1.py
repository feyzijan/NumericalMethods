#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Feyzi Can Eser
#
# Created:     15.04.2020
# Copyright:   (c) Feyzi Can Eser 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


A = [[1,2,3,4,5] , [6,7,8,9,10], [11,12,13,14,15]]





def AAT(A): # Returns the matrix multiplied with its transpose

    #Determine row and column number and create ranges
    r = len(A)
    Rr = range(0,r)
    c = len(A[0])
    Rc = range(0,c)

    AT = [] # transpose
    for j in Rc:
        t = [] #temporary matrix
        for i in Rr:
            t = t + [A[i][j]] #all elements in a single column are added to t
        AT = AT + [t] # t is added as a row to AT

    C =[] # Matrix Mulitplication
    #C's dimensions will be r by r


    for i in Rr: #  for every row in A
        t = []
        for k in Rr: # for every column in b
            x = 0 # temporary sum
            for j in Rc: # for every column in every row in A
                x = x + (int(A[i][j]))* int(AT[j][k]) #ie. A[0][0]*AT[0][0] + A[0][1]*AT[1][0] + A[0][2]*AT[2][0]....
                #then A[0][0]*AT[0][1] + A[0][1]*AT[1][0]
            t += [x]
        C += [t]


    for row in AT:
        print(row)

    print('C')
    for row in (C):
        print(row)

    return C



AAT(A)