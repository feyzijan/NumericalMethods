#-------------------------------------------------------------------------------
# Name:        module2
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

  #Task B: Write a script to generate a N x N matrix, with alternating 1s and 0s
  # of size 11x11 and then write the matrix dimensions and every single entry that into a text file



Rn = range (0,11)
M = []
temp = []

for i in Rn:
    Temp =[] # Create a Temp list of with 11 elements each of which is -1 or 1
    for j in Rn:
        a = ((-1)**j)*((-1)**i) # This ensures that each row is composed of alternating -1 and 1 values,
        # (-1)**i term ensures that odd numbered rows start with a 1 and even numbered ones with -1
        Temp = Temp + [a] # Add the temp to A as a single row
        #process is repeated by the number of rows
    M = M + [Temp]

##for row in M:
##  print(row)


# now simply turn negative values to 0
for i in Rn:
    for j in Rn:
        if M[i][j] == -1:
            M[i][j] = 0

for row in M:
    print(row)



# Now write this matrix into a text file

f = open('ChessBoard.txt', 'w')

f.write(str(len(M)))
f.write(str(len(M[0])))
for i in Rn:
    for j in Rn:
        f.write(str(M[i][j]))

f.close()

# how to make them each go on spereate lines








