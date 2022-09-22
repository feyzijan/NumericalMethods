#-------------------------------------------------------------------------------
# Name:        module1
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
# n! = n(n-1)!

def fact(n):
    if n == 0:
        f = 1
    else:
        f = n.fact(n-1)
        return f




