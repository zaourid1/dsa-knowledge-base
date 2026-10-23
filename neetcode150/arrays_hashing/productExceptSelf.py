"""
medium level.
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
"""

def productExceptSelf(nums):
    l = []
    p = []
    s = []
    for i in range(len(nums)):
        p = nums[:i]
        s = nums[i+1:]
        m = 1
        for a in range(len(p)):
            m *= p[a]
        for a in range(len(s)):
            m *= s[a]
        l.append(m)

    return l

nums = [1,2,4,6]
#print(productExceptSelf(nums))

def productExceptSelf_optimized(nums):
    """
    calculate from left then from right and multiply them
    """
    l = [1]*len(nums)
    left = [1]*len(nums)

    right = [1]*len(nums)
    
    for i in range(1,len(nums)):
        left[i] = left[i-1]*nums[i-1]
    
    for i in range(len(nums) - 2, -1, -1):        
        right[i] = right[i+1]*nums[i+1]
   
    for i in range(len(nums)):
        l[i] = left[i] * right[i] 
    return l

nums = [2,3,4,5]
print(productExceptSelf_optimized(nums))