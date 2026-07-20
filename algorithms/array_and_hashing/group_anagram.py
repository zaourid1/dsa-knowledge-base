"""
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
"""
def groupAnagrams(strs):
        hash1 = {}
        for word in strs:
            print(word)
            for letter in word:
                print(letter)
                '''
                if letter in hash1:
                    hash1[letter] += 1
                else:
                    hash1.update({letter: 1})
                '''
        final = []
        
        print(hash1)