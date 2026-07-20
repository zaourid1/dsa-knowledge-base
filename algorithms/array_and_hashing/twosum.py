"""
Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
"""

def twoSum (nums, target):
        hashm = {}
        hashm = nums
        print("Hash: ", hashm)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashm:
                if i != nums.index(diff):
                    return i, nums.index(diff)
                else:
                     for j in range(len(nums)):
                        if nums[j] == target and j!= i:
                            return i,j


nums = [3,4,5,6]
target = 7

print(twoSum(nums, target))

nums=[5,5]
target=10

print(twoSum(nums, target))