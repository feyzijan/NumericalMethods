#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      fce19
#
# Created:     08/11/2019
# Copyright:   (c) fce19 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

import random as rn
import math as mt
import matplotlib.pyplot as plt

if __name__ == '__main__':
    main()




# Purpose: Practise Random Generators

# Task A: Counted Loops

# Task 1
# Read an input and print a lne that many times
##N = input( 'Type the number of repetitions you want: ')
##N = int(N)
##R = range (0, N+1)
##for i in R:
## print("“I need to comment my scripts. Comments are marked too!")

# Task 2
# Find the sum of the squares of all numbers from 1 to n
##N = input( 'Type a number : ')
##N = int(N)
##R = range (0, N+1)
##sum = 0
##for i in R:
##    sum = sum + i**2
##print("The sum is: ", sum )
##print("The sum is: {} ".format(sum))

# Task 3
# Throw a dice N times and compute the overall score
##N = input('How many times would you like to roll a dice:')
##N = int(N)
##R = range (0, N+1)
##sum = 0
##for i in R:
##    dice = int(rn.random()*6 +1)
##    print(dice)
##    sum = sum + dice
##sum = sum/i
##print(' The overall score is : {}'.format(sum))
##
# Task 4
# Compute the factorial of a given integer
##N = input('Give me a number:')
##N = int(N)
##fact= 1
##for i in range(N, 0, -1):
##    fact = fact * i
##print(' The factorial of : {}'.format(N), 'is: {}'.format(fact))

# Task B: Conditional Flow
# Task 1: Throw dice and establish the winner
##P1 = input(' Name of Player 1:')
##P2 = input(' Name of Player 2:')
##P1dice = int(rn.random()*6+ 1)
##P2dice = int(rn.random()*6+ 1)
##print (' P1 threw: {}'.format(P1dice))
##print (' P2 threw: {}'.format(P2dice))
##
##if P1dice == P2dice:
##    print('It`s a draw')
##else:
##    if P1dice > P2dice:
##        print('The winner is', P1)
##    else:
##        print('The winner is', P2)

# Task 2
##P1 = input(' Name of Player 1:')
##P2 = input(' Name of Player 2:')
##N = input('How many times should they throw the dice:')
##N = int(N)
##P1score = 0
##P2score = 0
##draw = 0
##
##for i in range(0, N):
##    P1dice = int(rn.random()*6+ 1)
##    P2dice = int(rn.random()*6+ 1)
####    print (' P1 threw: {}'.format(P1dice))
####    print (' P2 threw: {}'.format(P2dice))
##    if P1dice == P2dice:
####        print('It`s a draw')
##        draw = draw + 1
##    else:
##        if P1dice > P2dice:
##            P1score = P1score + 1
##        else:
##            P2score = P2score + 1
##
##if P1score > P2score:
##    print('Player', P1,' won : {}'.format(P1score),' games.')
##    print('Player', P2,' won only : {}'.format(P2score),' games.')
##    print('The game was drawn: {}'.format(draw), 'times')
##else:
##        print('Player', P2,' won  : {}'.format(P2score),' games.')
##        print('Player', P1,' won only: {}'.format(P1score),' games.')
##        print(' The game was drawn: {}'.format(draw), 'times')
##
##




# Task 3: Rock Paper Scissors

##ply = input('Rock (1), Paper (2), or Scissors (3):')
##ply = int(ply)
##comp = int(rn.random()*3+1)
##print('Computer chose: {}'.format(comp))
##if ply == comp:
##    print( 'It"s a draw')
##else:
##    if ply ==1 and comp ==2 :
##        print('Computer Wins')
##    if ply ==1 and comp ==3 :
##        print('Player Wins')
##    if ply ==2 and comp ==1 :
##        print('Player Wins')
##    if ply ==2 and comp ==3 :
##        print('Computer Wins')
##    if ply ==3 and comp ==1 :
##        print('Computer Wins')
##    if ply ==3 and comp ==2 :
##        print('Player Wins')
##

#Task C
N = input('Give me a number:')
N = int(N)
for i in range (0, N+1):
    x = rn.random()
    y = rn.random()
    if (x**2 + y**2)< 0.25:
        plt.scatter(x,y)



### Task D
##N = input('Give me a number:')
##N = int(N)
##primeCount = 0
##for possiblePrime in range (2, N+1):
##    isPrime = True
##    for y in range(2, possiblePrime):
##        check = possiblePrime % y
##        if check == 0:
##            isPrime = False
##
##    if isPrime == True:
##        primeCount = primeCount + 1
##        print(possiblePrime)
##print('Prime Count is : {}'.format(primeCount))
##


##for i in range(0,10):
##    n = rn.random()*6-6
##    print(n)






