#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Feyzi Can Eser
#
# Created:     18.04.2020
# Copyright:   (c) Feyzi Can Eser 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()




f = open('FTSE100.txt','r')
a = f.readlines()


A = []
for item in a:
    A += [item.rstrip()] # write al llines into list A with trailing new lines stripped



Names = []
for i in range(0,len(A),3):
    Names += [A[i]]
    
ShareP = []
for i in range(1,len(A),3):
    ShareP += [float(A[i])]
    
ShareN = []
for i in range(2,len(A),3):
    ShareN += [int(A[i])]
    
    
l = len(Names)



L = []

for i in range(0,l):
    t = (Names[i],ShareP[i],ShareN[i])
    L += [t]
    

print(type(L[2][0]))


           
def Sort_Tuple(L):  
      
    # getting length of list of tuples 
    l = len(L)  
    for i in range(0, l):  
          for j in range(0, l-i-1):  
              if (L[j][1] > L[j + 1][1]):  
                  L[j], L[j+1]= L[j + 1], L[j]  
    return L
  

print(Sort_Tuple(L))  

p = 0

for i in range(0,len(L)):
    p += (L[i][1] * L[i][2])/1000000000

print('Total value in billion dollars is ' + str(p))
