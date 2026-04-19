"""
Problem 1: Given an array of int A[0....n-1] find max value of 
A[j] - A[i] where j > i.
"""

def max_bruteForce(n):
    # n is an array of int
    l = len(n)
    maxdiff = 0
    for i in range(l):
        for j in range(i+1,l):
            d = n[j] - n[i]
            if d > maxdiff:
                maxdiff = d
    return maxdiff

A = [2,3,10,6,4,8,1]

print(max_bruteForce(A))

"""
Now lets look for a reccurence and use DP
"""
def max_dp(n):
    maxP = 0
    l = len(n)
    for i in range(l):
        maxP = max(max_dp(n-1))
    return maxP