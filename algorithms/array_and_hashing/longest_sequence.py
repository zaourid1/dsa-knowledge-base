"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].
"""

def longestConsecutive(nums):
    sortedList = sorted(nums)
    print(sortedList)
    count = 0
    h = {}
    # h = {pos:value}
    for i in range(len(sortedList)):
        v = int(sortedList[i] - 1)
        #print(v)
        if v not in sortedList:
            #print(f'{v} not in list')
            h.update({i:sortedList[i]})
    print(h) 
              
    return count

nums = [2,20,4,10,3,4,5]
longestConsecutive(nums)

nums = [0,3,2,5,4,6,1,1]
longestConsecutive(nums)
#7

nums = []
longestConsecutive(nums)