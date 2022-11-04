#-------------------------------------------------------------------------------
# Name:        module2
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
    import random as rn

#Task B: Write a function MatMat that receives two matrices A nd B of size MxN and NxP
# and returns the product C=AB, and return 0 if hey cant be multiplied



# Personal Task: Write a function to generate a matrix of a given size

def GenMat (r,c):
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


# Generate Matrices and print tem out
A = GenMat(5,4)

B = GenMat(4,3)

print('A')
for row in A:
    print (row)

print('B')
for row in B:
    print(row)


# Now onto the main Task

def MatMat (A,B):
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
            t = 0 # initilaise temporary sum
            for j in Rca: # for every column in every row in A
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






print('C')
for row in (MatMat(A,B)):
    print(row)





