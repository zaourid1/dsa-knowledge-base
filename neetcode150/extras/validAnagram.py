"""
Notes: trying to find a faster way to solve this problem. 
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, regardless of order.
Example 1:
    Input: s = "racecar", t = "carrace"
    Output: true
"""
def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    hash1 = {}
    hash2 = {}
    for i in s:
        pass
    

s = "racecar" 
t = "carrace"
print(isAnagram(s,t))