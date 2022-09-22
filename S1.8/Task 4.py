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

# Task 4: Write a function that transposes a given matrix


# First make the matrix

##M = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
##
##for row in M:
##    print (row)



def Transpose(M):
    Ri = range(0,len(M))
    Rj = range(0, len(M[0])) # initiliase ranges for rows and columns
    T = []
    for j in Rj:
        temp = []
        for i in Ri:
            temp = temp + [M[i][j]] #  the first,second,trird... element of each row is added to a temp list
            # this temp list is added to tthe transpose matrix as a row
        T = T + [temp]
    return (T)


# read file and write everything in a list
f = open('Trans.txt','r')
a = f.readlines()
A = []
for item in a:
    A = A + [int(item)]

# take the matrix sizes out from the list
rnum = A[0]  #row number
cnum = A[1]  #column number

#remove the dimesnions from the list
A.pop(0)
A.pop(0)

print(rnum)
print(cnum)

print(len(A))



Am = []
print(A[5889])
print(A[5890])
print(A[5891])
print(A[5892])
print(A[98490])



Rr = (0, 402) # range of rows

for i in Rr:
    Rn = ((245*(i)), (245*(i+1)), 1)
    Temp = []
    for j in Rn:
        print(j)
        Temp = Temp + [int(A[j])]
    Am += [Temp]

print(Transpose(Am)[11][25])







