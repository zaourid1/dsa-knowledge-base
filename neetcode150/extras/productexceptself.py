"""
Date: 10/18/2026 Author: Zineb Aourid
Given an integer array nums, return an array output where output[i]
is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.
Example 1:
    Input: nums = [1,2,4,6]
    Output: [48,24,12,8]
Example 2:
    Input: nums = [-1,0,1,2,3]
    Output: [0,-6,0,0,0]
Goal(O(n) time)
"""

def productExceptSelf(nums):
    """
    my intuition is to go over the list but that would cause higher time then 
    O(n).
    """
    results = [None]*len(nums)
    print(results)
    prefix = []
    suffix = []
    for i in range(len(nums)):
        print("nums[i]: ",nums[i], nums)
        #print(i)
        prefix = nums[:i]
        suffix = nums[i+1:]
        print(f"pre: {prefix}, suf: {suffix}")
        results[i] = prefix[i]*suffix[i]
        print(results)
    #results.append(prefix)

    return results

nums = [1,2,4,6]
print(productExceptSelf(nums))