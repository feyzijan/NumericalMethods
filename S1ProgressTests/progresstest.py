#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      fce19
#
# Created:     10/01/2020
# Copyright:   (c) fce19 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

##
##N = open('Numbers.txt', 'r')
##n = N.readlines()
##
##numbers = []
##
##for item in n:
##    numbers += [int(item)]
##
##
##
##Rn = range(0, len(numbers))
##
##count = 0
##
##for i in Rn:
##    if (numbers[i] > 54) and (numbers[i] < 80) :
##        count +=1
##
##print(count)
##
##a = 2
##a = (a,2,1)
##a = [a,(2,1),a]
##
##
##print(type(a))
##print(len(a))
##print(a)
##
##
##a = False
##b = 1
##cz = 0
##while not a and b <= 500:
##    b += 2
##    if b < 100:
##        b += 3
##        cz += 1
##    else:
##        b += 2
##        cz += 1
##
##print(cz)


Na = int(input('give me n'))

y = 0
ya = 0
yb = 0


Rnn = range(0,15)
condition = False

while condition == False:
    for j in Rnn:
        ya = 1/(4**j)
        yb = 1/ (4**(j +1))
        if ((ya - yb) < 0.0005):
            print(j)
            condition = True






