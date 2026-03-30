"""
You are climbing a staircase. It takes n steps to reach top.
Each time you can climb:
    1 or 2 steps. 
In how many distict ways can u reach the top?

e.g.
n = 2 OutPut = 2
1. 1 step + 1 step
2. 2 steps
Output = 2

n = 3 OutPut = 3
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

n = 4 OutPut = 5
1. 1 + 1 + 1 + 1 (1 + cS(n-1))
2. 1 + 2 + 1
3. 1 + 1 + 2
4. 2 + 1 + 1 (2 + cS(n-2))
5. 2 + 2

3 + cs(n-3)...
Hint: find recusrsion first, identify base cases, check for over lapping subproblems

"""

def clibmingStairs(n):
    #Base case if n = 1, return 1
    if n <= 3:
        return n
    
    curr = 0
    prev1 = 3
    prev2 = 2 

    for i in range(3,n):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr
    return curr

print(clibmingStairs(4))