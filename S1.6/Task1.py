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
# Task 1: Write a factorial functioon

def Factorial(a):
    Rn =range(0,a)
    af = 1
    for i in Rn:
        af = af * (a-i)
    return af


a = int(input('Give me a number'))
print(Factorial(a))

