#-------------------------------------------------------------------------------
# Name:        module2
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



# Task 1: Recursive Fibonacci Sequence

def Fibonacci(n):
    if n == 1 or n== 2:
        return 1
    else:
        n = Fibonacci(n-1) + Fibonacci(n-2)
        return n



N = 27
Rn = range(1,N+1)

for i in Rn:
    print(Fibonacci(i))
