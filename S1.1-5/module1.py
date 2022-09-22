#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      feyzi
#
# Created:     09/01/2020
# Copyright:   (c) feyzi 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import math as mt
import matplotlib.pyplot as pl

# Task 1: Expand sinx where 0<x<2p with taylor series with step 0.01 for a given N


N = int(input('Give me N'))

dx = 0.01
xp= []
yp= []
x = 0
y = 0

Rn = range(1, N+1 ,2)

while x <= (mt.pi)*2:
    for i in Rn:
        y = (((-1)**int(i/2))*(x**i)/(mt.factorial(i)))
        xp = xp +[x]
        yp = yp + [y]
    x = x + dx


pl.scatter(xp,yp)

print(yp)














# Task 2:







# Task 3:







# Task 4: Find thea bsolute minimum of a function




# Task 5: Find relative minima of a function







# Task 6: Input a word and establish if it is palindrome







# Task 7: Read a Budget file and organize the data in a list of tuple
# (month, total expenses, total incomes)
# Compute the total savings for each month and store them in a file Savings.txt


##B = open('Budget.txt', 'r')
##b = B.readlines
##
##
##Months = []
##Tex = []
##Tin = []
##
##Rn= range(0,len(b))
##
##for item in b:
##    if item is float:
##














#Task 8: