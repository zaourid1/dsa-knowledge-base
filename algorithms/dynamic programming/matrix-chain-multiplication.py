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

print(catalan(20))

"""
We will try do this using memozation dynamic programming method (top-down)
"""