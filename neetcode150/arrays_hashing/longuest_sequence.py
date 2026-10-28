"""
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.
Example 1:
    Input: nums = [2,20,4,10,3,4,5]
    Output: 4
"""
def longestConsecutive(nums):
        sorted_list = sorted(nums)
        print(sorted_list)
        seq = 0
        for i in nums:
            pass

print(longestConsecutive(nums=[2,20,4,10,3,4,5]))