"""
Input: nums = [1,2,4,6]

Output: [48,24,12,8]
"""

def productExceptSelf(nums):
    multiplier = 1
    for i in nums:
        if i != 0:
            multiplier *= i
    
    print(multiplier)

    l = [1]*len(nums)
    print(l)
    
    for i in nums:
       if i == 0:
            for j in nums:
                l.append(0)
            l[i] = multiplier
        else:
            l.append(multiplier/i)
    
   

    return l

nums = [1,2,4,6]
print(productExceptSelf(nums))

nums=[-1,0,1,2,3]
print(productExceptSelf(nums))
# expected: [0,-6,0,0,0]