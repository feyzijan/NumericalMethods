#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      fce19
#
# Created:     06/03/2020
# Copyright:   (c) fce19 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

   #Task C: Write a boolean function that receives two strings and determines whether
    #one is an anagram of the other

    # Anagram:An anagram is a word or phrase formed by rearranging the letters of a
    # different word or phrase using all the original letters exactly once


a = 'nero'
b = 'eron'


def split(word): # *** Function that splits a string into a list of characters
    return [char for char in word]

A = split(a)

n = ord('a') - 96  #********* ord('') returns the alphabetical order + 96 of a letter
print(n)

def IsAnagram(a,b): # ********WORDS MUST BE LOWERCASE******

    def split(word): # Define the split functin inside the anagram function
        return[char for char in word]

    # Split both strings into letters
    A = split(a)
    B = split(b)

    # if their lengths dont equal, they cant be anagrams
    if (len(A) != len (B)):
        return False

    # convert each letter into a number that is its position in the alphabet
    An = []
    Bn= []

    # sort the lists of letters aphabetically
    A.sort()
    B.sort()
    print(A)
    print(B)


    for i in range(0,len(A)): # Convert each letter to a value
        ta = 0
        tb = 0
        ta = ord(A[i])
        tb = ord(B[i])
        An += [ta]
        Bn += [tb]

    print(An)
    print(Bn)

    if An == Bn: # F the lists are identical there is an anagram
        return True
    else:
        return False




print(IsAnagram(a,b))



