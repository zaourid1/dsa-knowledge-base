"""
Activity Selection Problem Using Brute-Force (Runtime: O(2^n))

Input: List = [(s1,f1),(s2,f2),.... (sn,fn)]
where Si = start time of activity i
      Fi = finish time of activity j
Output: max # of activities, such that there is no overlapping activities.
"""

a = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)]

def subsetting(L):
    """
    Given an integer array nums of unique elements, return all possible subsets (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.
    """
    result = [[]]
    for num in L:
        result += [curr + [num] for curr in result]
        #print(result)
    return result

a = [(1,4)(3,5)(5,7)]
print(subsetting(a))

def activitySelec(L):
    subset = subsetting(L)
    maxCount = 0
    for i in subset:
        for j in i:
            pass
    return 0