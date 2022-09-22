#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      fce19
#
# Created:     22/11/2019
# Copyright:   (c) fce19 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()



# Task A
# Read CID numbers and marks from two files.
# Calculate average and maximum marks
##
##    M = open('Marks.txt', 'r')
##    C = open('CIDs.txt', 'r')
##
##    c = C.readlines()
##    m = M.readlines()
##
##    Marks = []
##for item in m:
##    Marks = Marks + [int(item)]
##
##CIDs = []
##for item in c:
##    CIDs = CIDs + [int(item)]
##
##
##max = 0
##sum = 0
##
##R = range(0, (40))
##
##for i in R:
##        sum = sum + int(Marks[i])
##        if (int(Marks[i]) > max):
##            max = int(Marks[i])
##
##average = sum/40
##
##
##print(" Max is : {}" .format(max))
##print("Average is: {}" .format(average))
##
##M.close()
##C.close()




# Task B
# Search for values in a list- Type CID and display the score of a student
# Display students with highest marks and save the list in a new file

##find = int(input(' Type CID Number to learn the student`s score'))
##count = 1
##found = False
##
##
##while (not found):
##    if count < len(CIDs):
##        if CIDs[count] == find:
##            found = True
##            print("Score is : {}" . format(Marks[count]))
##        else:
##            count = count + 1
##    else:
##        print("CID invalid")
##        break


##maxlist = []
##R = range(0, (len(Marks)-1), +1)
##
##for i in R:
##    if max == int(Marks[i]):
##        maxlist = maxlist + [CIDs[i]]
##        continue
##
##
##print(maxlist)
##
##b = open('Best.txt','w')
##
##for item in maxlist:
##    b.write(str(item)+'\n')
##
##b.close()




##
### Task C
### Series Expansion
##
import matplotlib.pyplot as pl

Col = ['Red' , 'Blue' , 'Green' , 'Cyan']
dx = 0.01
RN = range(2,15,4)

# Iterate for every N
for N in RN:
    # that is for N = 2,6,10,14
    # setting the range of i , from 0 to N

    Ri = range (0,N+1)

    x =[]
    y =[]
    # Traverse the range of x
    xc = -0.8
    while xc <= -0.08:
        # itereate until you reach the upper boundary of x
        #evaluate y for current x
        # initalise the sum
        yc = 0
        for i in Ri:
            yc = yc + xc**i

        # store the current evaluated x and y values
        x = x + [xc]
        y = y + [yc]

        # update the value of x
        xc = xc + dx

        pl.scatter(x,y,s=2, c = Col[N//4])

        #evaluate and plot the analytical y(x)
        for val in x:
            yex = 1/ (1-val)
            pl.scatter(val, yex, s=4, c ='Black')





##
##
### Task D
###
##x = 2
##while not (-1< x< 1):
##    x = input('Type a number between -1 and 1')
##    x = float(x)
##
##Q = input('Give me Q')
##Q= float(Q)
##
##i = 0
##
##Sum = 0
##
### We keep adding terms until the accuracy is larger than the desired one
### We want |y(n+1) - y(n)| > 10^-Q
### Note that |y(n+1) - y(n)| = x^(n+1) ??????
##
##while abs (x**(i+1)) > 10 **(-Q):
##    #add anotehr term
##    Sum = Sum + x**i
##    # update counter
##    i = i+1
##
##    print ('Terms: ' + str(i))
##    #compute exact value
##    yexact = 1/(1-x)
##    error = yexact - Sum
##    print(Sum)
##    print(yexact)
##    print(error)
##
