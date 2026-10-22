"""
Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    new_s = sorted(s)
    new_t = sorted(t)

    if new_s == new_t:
        return True

    return False

s = "rat"
t = "car"
print(isAnagram(s,t))

s = "anagram" 
t = "nagaram"
print(isAnagram(s,t))

def isAnagram_optimized(s,t):
    """
    can i write this in O(n) time? hint: use a dict
    """
    if len(s) != len(t):
            return False

    h1 = {}
    h2 = {}

    for i in s:
        if i not in h1:
            h1[i] = 1
        else:
             h1[i] += 1
    for i in t:
        if i not in h2:
            h2[i] = 1
        else:
            h2[i] += 1

    if h1 == h2:
        return True

    return False
         
    print(h1)

s = "anagram" 
t = "nagaram"
print(isAnagram_optimized(s,t))