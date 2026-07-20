"""
Given an integer array nums, return true if any value appears
more than once in the array, otherwise return false.
"""

def duplicates_bruteForce(l):
    """
    essentialy O(n2) so very slow...
    """
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] == l[j]:
                return True
    return False

nums = [1,2,3,3]
print(duplicates_bruteForce(nums))
 
n = [0,1,2,3]
print(duplicates_bruteForce(n))

def duplicates(l):
    """
    lets try using a hash table
    """
    hast = {}
    for i in l:
        if i not in hash:
            hash.
    return