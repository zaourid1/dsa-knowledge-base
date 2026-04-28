"""
Leetcode 561 Problem
Given an array of 2n int, return max sum of min pairs.
E.g.
Input: nums = [1,4,3,2]
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4

So the maximum possible sum is 4.
"""

def arrayPairSum(nums):
    """
    my greedy intution is to sort nums from biggest to smallest and pair big nums tg and take their min.
    """
    sortedA = sorted(nums, reverse=True)
    pairs = list(zip(sortedA[::2], sortedA[1::2]))
    total = 0
    for i in pairs:
       minimum = min(i)
       total += minimum
    return total

a = [1,4,3,2]
print(arrayPairSum(a))