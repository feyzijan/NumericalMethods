#-------------------------------------------------------------------------------
# Name:        module4
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


# Task 3: Create a script that creates a NxN matrix with the pattern of the scottish flag

N = int(input('Give me N'))


Rn = range (0,N)


A = []


Temp = []



for i in Rn:
    Temp = []
    for j in Rn: # Create a Temp list of with N elements each of which is 0
        Temp = Temp + [0]
    A = A + [Temp] # Add the temp to A as a single row
 # Create a list of NxN size with all values set to 0

for k in Rn:  # i.e. [5][5]--[4][4]..... are set to 1
    A[k][k] = 1


Rr = range (N-1, -1, -1)
for k in Rr: # k goes 5-4-3-2-1-0
    A[k][N-1-k] = 1 #i.e. [5][0]--[4][1]..... are set to 1






for row in A:
    print(row)

