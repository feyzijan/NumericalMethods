#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Feyzi Can Eser
#
# Created:     16.04.2020
# Copyright:   (c) Feyzi Can Eser 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()



A = [[1,2,3,4], [5,6,7,8] , [9,10,11,12], [13,14,15,16]]



def MatMat (A,B): #Matrix multiplicaiton function from Exercise 9-B
    if len(A[0]) != len(B):
        return 0
    #define row and column ranges
    Rra = range(0,len(A))
    Rca = range(0,len(A[0]))
    Rrb = Rca
    Rcb = range(0,len(B[0]))

    C = []

    for i in Rra: #  for every row in A
        for k in Rcb: # for every column in b
            t = 0 # initialise temporary sum
            for j in Rca: # for every column in each row in A
                t += (A[i][j])* (B[j][k]) # sum the product of the elements in a row of A with those in a row of B
            C += [t] # add the sums(elements of the product matrix) to a new list

    # Now turn the product list into a matrix
    Cf = [] # initiliase product matrix
    # dimensions of this is lenA x lenB[0]

    for i in Rra:
        Rn = range((i*len(B[0])), ((i+1)*len(B[0]))) # i.e. range is moving 0-5, 5-10, and each range is a row
        t = []
        for j in Rn:
            t += [C[j]]
        Cf += [t]

    return Cf




def GenMat (r,c): # Matrix generator from previous Task
    import random as rn
    A = []
    Rr = range(0,r)
    Rc = range(0,c)
    for i in Rr:
        t = []
        for j in Rc:
            t = t + [rn.randint(0,10)]
        A = A + [t]
    return A




def MatOp (A):
    print('Function MatOp started')

    if len(A) != len(A[0]): # check if matrix is swuare
        return 0

    C = [] # lower triangular
    D = [] # diagonal
    E = [] # Upper triangular
    T = [] # CD + ED

    a = len(A)
    Ra = range(0,a) # set up the range of rows and columns

# MATRIX D
    for i in Ra: # Create a D matrix with same size as A but all values being zero
        t = []
        for j in Ra:
            t = t + [0]
        D = D + [t]



    for i in Ra: # Replace 0's with values from A to form diagonal matrix
        D[i][i] = A[i][i]
    print('D') # print to check
    for row in D:
        print(row)


# MATRIX C
    for i in Ra: # Create a C matrix with same size as A but all values being zero
        t = []
        for j in Ra:
            t = t + [0]
        C = C + [t]

    for i in range(1,a): # Insert Lower triangle values
        Rj = range(0,i)# range of columns increases with row number
        for j in Rj:
            C[i][j] = A[i][j]

    print('C') # print to check
    for row in C:
        print(row)

# MATRIX E

    for i in Ra: # Create a E matrix with same size as A but all values being zero
        t = []
        for j in Ra:
            t = t + [0]
        E = E + [t]


    for i in range(0,a):
        Rj = range(i+1,a) # range of columns decreases with row number
        for j in Rj:
            E[i][j] = A[i][j] # Replace zeros with values from A


    print('E') # print to check
    for row in E:
        print(row)


    P1 = MatMat(C,D)
    P2 = MatMat(E,D)

    print('P1')
    for row in P1:
        print(row)

    print('P2')
    for row in P2:
        print(row)

    T = []
    T = GenMat(a,a)


    for i in Ra:
        for j in Ra:
            T[i][j] = (P1[i][j] + P2[i][j])

    print('T')
    for row in T:
        print(row)

    return T






print('A')
for row in A:
        print(row)

MatOp(A)