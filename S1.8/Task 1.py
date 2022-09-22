#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      fce19
#
# Created:     21/02/2020
# Copyright:   (c) fce19 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

# Task 1: Create a function that multiplies a given matrix by a given vector

M = [[1,2,3,4,5], [2,3,4,5,6], [3,4,5,6,7], [4,5,6,7,8] ,[5,6,7,8,9], [6,7,8,9,10]]
V = [[1],[2],[3],[4],[5]]
# create matrix and vector to be sent to the function

def Matvec(M, V):
    # check to see if the matrices are fit for mmultplication
    # by checking in first matrix"s number of columns equals the others number of rows
    if len(M[0]) != len(V):
        return(0)

    C = [] # initilaise product matrix
    Ri = range(0,200)
    Rj = range(0,400)
    # initilaise ranges for columns and rows
    for i in Ri:
        C = C + [[i]] # create procut c with i rows, to be replaced by values later
##    for row in C:
##        print (row)

    for i in Ri: # for each row of the product
        tempsum = 0
        for j in Rj:
            a = M[i][j]
            b = V[j]
            temp = a*b
            tempsum += temp #sum up each multplication individually
        C[i][0] = tempsum # row equals the mult'pl'cation of row i of first matric by column j of second
    return(C)



# Read files and write all elements into list A and B
fa = open('Q1A.txt', 'r')
fb = open('Q1B.txt', 'r')
a = fa.readlines()
b = fb.readlines()
fa.close
fb.close

A = []
B = []

for item in a:
    A = A + [item]

for item in b:
    B = B + [item]

Am = []
Bm=[]

# A is a  200x400 matrix
# B is a 400x1 vector


#Below is a method for turning the lists A and B to matrices Am and Bm

Rr = range(0,200)
Rc = range(0,400)

for i in Rr:
    Rn = range ((400*(i)), (400*(i+1)), 1)
    Temp = []
    for j in Rn:
        Temp = Temp + [int(A[j])]
    Am = Am + [Temp]


# Relatively simple to create matrix Bm
for i in Rc:
    Bm = Bm + [int(B[i])]


# Print matrices just to check
##for row in Am:
##    print(row)
##
##for row in Bm:
##    print (row)



print(len(Am))
print(len(Am[0]))
print('')
print(len(Bm))



##for row in (Matvec(Am,Bm)):
##    print(row)

print(Matvec(Am,Bm))

print(len(Matvec(Am,Bm)))

print(Matvec(Am,Bm)[124])


