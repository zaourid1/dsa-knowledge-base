"""
attempting another medium leetcode
The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
"""

def topKFrequent(nums,k):
        h = {}
        l = []
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                h[i] += 1

        #found this online syntax for sorting dict
        sorted_v = dict(sorted(h.items(), key=lambda item: item[1], reverse=True))

        l = (list(sorted_v.keys())[:k])
        
        return l

nums = [1,2,2,3,3,3]
k = 2
print(topKFrequent(nums,k))
print()
nums=[7,7]
k=1
print(topKFrequent(nums,k))
