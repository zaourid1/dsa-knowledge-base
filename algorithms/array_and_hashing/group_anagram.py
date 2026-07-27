"""
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
"""
from collections import defaultdict

def groupAnagrams(strs):
        hash1 = defaultdict(list)
        for s in strs:
                count = [0]*26
                for c in s:
                    count[ord(c) - ord('a')] += 1
                    #print(count)
                hash1[tuple(count)].append(s)
               # print(hash1)
        return list(hash1.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))
