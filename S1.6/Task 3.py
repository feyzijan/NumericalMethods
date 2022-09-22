#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      feyzi
#
# Created:     11/01/2020
# Copyright:   (c) feyzi 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import random as random

# Task 3: Create a fucntion that sorts a given list in ascending order

S = open('Set.txt', 'r')


s = S.readlines()

Set = []

for item in s:
    Set = Set + [int(item)]






A = []
a = 0
Rn = range(0,51)
for i in Rn:
    a = random.randint(0,101)
    A = A +[a]
# Generate 50 random integers between 1-100 and store them in List A

##print(A)


def SortAscending(A):
    N = len(A)
    Rk = range(0,N)
    for k in Rk:
        Rm = range(k+1,N)
        for m in Rm:
            if (A[m] < A[k]):
                (A[m], A[k]) = (A[k], A[m])
    return A

#print(SortAscending(A))

SetO = SortAscending(Set)
print(SetO[88])

