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

    #import matplotlib

# Unfinished
# Task D: Read of hourly tempreature data for 10 days from a text file
# Plot the average temreature for each day in a graph and compute the max and min temperatures

    f = open('Temperatures.txt', 'r') # open text file
    a = f.readlines() # read lines
    f.close()
    A = []

    # type lines into a list of integers
    for item in a:
        A += [int(item)]

    #convert this into a 10 by 24 matrix for simplicity
    Am= []
    Rn = range(0,10)
    for i in Rn:
        Rr = range(24*i, 24*(i+1)) # Moving range i.e 0-24, 24-48, ....
        t = []
        for j in Rr:
            t += [A[j]] # Compute each row
        Am += [t] # Add each row to A


for row in Am:
    print(row)




# Compute the avearges for each day and store them in list Av
t = 0
Av = []

for i in range(0,10):
   for j in range(0,24):
        t += Am[i][j]
   Av += [t/24]

print(Av)

# list of days
D = [1,2,3,4,5,6,7,8,9,10]

# Plot Av vs D

#matplotlib.plot(Av,D)


# Compute the max and min values from A( which is the list of all the integers)
max = max(A)
min = min(A)

print(max)
print(min)

#****8 YOU MUST WRITE ASCRIPT  script to sort the list and find the max and min values

x = 0
t = 0
def FindMin(A): # A is a matrix
    Ra = range(0,len(A))
    Rb = range(0,len(A[0]))
    t = 0
    for i in Ra:
        for j in Rb:
            x = 0
            x = A[i][j]
            if x > t:
                t = x
    return(t)


def FindMax(A): # A is a matrix
    Ra = range(0,len(A))
    Rb = range(0,len(A[0]))
    t = 100
    for i in Ra:
        for j in Rb:
            x = 0
            x = A[i][j]
            if x < t:
                t = x
    return(t)

print('Min value is '  + str(FindMin(Am)))
print('Max value is '  + str(FindMax(Am)))



def SortAscending (A):
    Ra = range(0,len(A))
    Rb = range(0,len(A[0]))
    As = []

    for i in Ra:
        for j in Rb:
            x = A[i][j]
            As += [x]

    R = range(0,len(As))
    for i in R:
        for k in R:
            if As[i] < As[k]:
                As[i] , As[k] = As[k] , As[i]

    return(As)


print(SortAscending(Am))
print('Min value is '  + str(SortAscending(Am)[0]))
print('Max value is '  + str(SortAscending(Am)[-1]))













