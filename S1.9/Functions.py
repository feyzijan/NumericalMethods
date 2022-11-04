
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



    

# Turn into a function to read text file and transform to a matrix
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





