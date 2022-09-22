#-------------------------------------------------------------------------------
# Name:        module5
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


# Task 4: Create Matrices from two text files
#





def ReadMatrix(L): # function receives file _name ad matrix dimensions
    # Create a list with all the numbers from a given file
    x = open(L[0], 'r')
    X = x.readlines()
    x.close()
    Xn = []
    for item in X:
        Xn = Xn +[int(item)]


    A = []

    Rc = range(0,L[1]) # Range of rows
    for j in Rc:
        Rr = range(L[2]*j,L[2]*j+L[2],1) # range of colums
        Temp = []
        for i in Rr: # i goes from 0-60 to 60-120 storing each set of 60 numbers in a temp list
            Temp = Temp + [Xn[i]]
        A = A + [Temp] # Adds the temp list of 60 values to A as a single row/element

    return A



# execute functions and print the returned list

La = ['MatA.txt', 60,60]
A = ReadMatrix(La)
##for row in A:
##        print(row)


Lb = ['MatB.txt',60,60]
B = ReadMatrix(Lb)
##for row in B:
##        print(row)



C = []
N = 60


RN = range(0,N)

for i in RN:  # compute row i
    row =[]  # initilaise row i
    for j in RN: # compute column j in row i
        row += [A[i][j] + B[i][j]]
        C += [row] # add row i to matrix C




for row in C:
    print(row)



print(C[24][19])



