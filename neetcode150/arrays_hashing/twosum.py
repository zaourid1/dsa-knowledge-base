"""
Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
"""

def twoSum(nums, target):
    for i in range(len(nums)):
        c = target - nums[i]
        
        for j in range(i+1,len(nums)):
            if nums[j] == c:
                return[i,j]

        

nums = [3,4,5,6]
target = 7

print(twoSum(nums, target))

nums = [5,5]
target = 10

print(twoSum(nums, target))

def twoSum_optimized(nums, target):
    """
    can i optimize this to O(n) time?
    """
    seen = {}
    #dict to keep track of nums + indices

    for i, num in enumerate(nums):
        c = target - num

        if c in seen:
            return[seen[c],i]
        seen[num] = i

nums = [3,4,5,6]
target = 7

print(twoSum_optimized(nums, target))