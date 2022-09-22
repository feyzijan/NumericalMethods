#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      fce19
#
# Created:     25/10/2019
# Copyright:   (c) fce19 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#Task 1 Creating Lists


A = [10, 11, 12, 13, 14 ,15 , 16 , 17 ,18 ,19 , 20]
B = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
c = A[2] + A[3]
B[4] = c
B[5] = B[5] * 2
print (c)
print(B[5])
first = A[0]
last = A[10]
A[0] = last
A[10] = first
print("A0 IS " + str(A[0]))
print (A[10])
i = 3
j = 5

iindex = B[i]
jindex = A[j]

B[i] = jindex
A[j] = iindex

print(B[i])
print(A[j])
print("\n")




## Task 2 Generating Lists

A= []

R = range(1,101)


for i in R:
    A = A + [i]

print ("A is " + str(A))

print("\n")

B = []

R = range (0,100)

for i in R:
    B = B + [(A[i])**2]

print ("B is " + str(B))
print("\n")

C = []

R = range (0,100)

for i in R:
    C = C + [(A[i] + B[i])]

print ("C is" + str(C))
print("\n")
print ("C9  is " + str(C[9]))


## Task 3 Managing Lists


N = len(A)

R = range(0, N, +3)

print (R)
print("\n")

for i in R:
    A[i] = 0


print ("A is " + str(A))
print("\n")


D = []

R = range (0, 100)

for i in R:
    D = D + [(A[99-i])]


print ("D is " + str(D))
print("\n")
print("D9 is " + str(D[9]))

## Task D Maths and Plotting Functions

import math


R = range (1, 101, +5 )

X = []

for i in R:
    X = X + [i]




print("X is " + str(X))














