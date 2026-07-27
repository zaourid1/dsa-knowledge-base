"""
Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
"""
def topKFrequent(nums, k):
    count = {}
    #print(count)
    for i in nums:
        if i not in count:
           #print(i)
           count.update({i:1})
           #print(count)
        else:
            #print("number already in count")
            count[i] += 1
    print(count)
    sorted_count = sorted(count.items(), key=lambda item: item[1], reverse=True)
    print(sorted_count)

    l = []

    values_only = [item[0] for item in sorted_count]
    for i in range(k):
       l.append(values_only[i])

    
    return l
        
nums = [1,2,2,3,3,3]
k = 2
#print(topKFrequent(nums, k))

nums=[1,1,1,2,2,3]
k=2
print(topKFrequent(nums, k))