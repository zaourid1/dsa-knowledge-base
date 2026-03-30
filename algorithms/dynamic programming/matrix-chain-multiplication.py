"""
Finding Catalan Numbers
The formula is simple: 
    We let P(n) = # of full paranthesis of n matrices to find reccurence:
    Base Case: P(1) = 1
    or P(n) = sum(k=1 to n-1) P(k) * P(n-k) if n >= 2
"""

def catalan(n):
    """
    let n = num of matirces
    this is using recursive method.
    """
    if n == 1:
        return 1
    
    numP = 0
    for i in range(1,n):
        #print(i)
        numP += catalan(i) * catalan(n-i)
    return numP

#print(catalan(10))

"""
We will try do this using bottom-up mehtod dynamic programming method
"""

def catalan_bottomup(n):
    if n == 1:
        return 1

    dp = [0] * (n)
    dp[0] = 1

    print(dp)
    for i in range(1,n):
        print("I: ", i)
        k = i
        dp[i] = dp[k] * dp[i-k]
    
    print(dp)

#catalan_bottomup(5)


"""
Here we will start looking at matrices, first is printing the indinces. 
"""
def indices(a,b):
    """
    A matrix[a,b] with dimension i * j
    i = # of cols
    j = # of rows
    """
    for i in range(a):
        for j in range(b):
            if j > i:
                print(i,j)

indices(2,3)