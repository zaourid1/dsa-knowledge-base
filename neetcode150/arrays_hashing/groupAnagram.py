"""
medium level problem (first attempt at a medium)

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
"""

def groupAnagrams(strs):
    """
    my thought process is using a dict to keep track
    """
    d = {}
    l = []

    for i in strs:
        sorted_i = "".join(sorted(i))

        if sorted_i not in d:
            d[sorted_i] = [i]
        else:
            d[sorted_i].append(i)
  
    for i in d:
        l.append(d[i])

    return l

strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))
#[["hat"],["act", "cat"],["stop", "pots", "tops"]]