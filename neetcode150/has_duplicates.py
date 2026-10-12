"""
Notes: previously solved problem.. level easy.
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
Example 1:
    Input: nums = [1, 2, 3, 3]
    Output: true
"""
def hasDuplicate(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False

       
nums = [1, 2, 3, 3]
print(hasDuplicate(nums))
nums = [1, 2, 3, 4]
print(hasDuplicate(nums))