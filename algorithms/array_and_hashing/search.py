"""
Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in 
O
(
l
o
g
n
)
O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
""" 

def search(nums, target):
        
        t_middle = int(len(nums) / 2)
        if t_middle == 0:
            return -1 

nums = [-1,0,2,4,6,8]
target = 4
print(search(nums, target))