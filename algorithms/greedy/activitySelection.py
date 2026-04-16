"""
Activity Selection Problem Using Brute-Force (Runtime: O(2^n))

Input: List = [(s1,f1),(s2,f2),.... (sn,fn)]
where Si = start time of activity i
      Fi = finish time of activity j
Output: max # of activities, such that there is no overlapping activities.
"""

a = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)]

def is_valid(subset):
    for i in range(len(subset)):
        for j in range(i+1, len(subset)):
            s1, f1 = subset[i]
            s2, f2 = subset[j]

            # TODO: check overlap
            if f1 > s2 and f2 > s1:
                return False
    return True


def generate_subsets(activities, index, current, result):
    if index == len(activities):
        result.append(current[:])
        return

    # include
    current.append(activities[index])
    generate_subsets(activities, index+1, current, result)

    # exclude
    current.pop()
    generate_subsets(activities, index+1, current, result)


def brute_force_activity(activities):
    subsets = []
    generate_subsets(activities, 0, [], subsets)

    max_count = 0

    for subset in subsets:
        if is_valid(subset):
            max_count = max(max_count, len(subset))

    return max_count

print(brute_force_activity(a))

"""
Using a greedy algorithm #1
Steps:
1. sort in order of start time. S = []
2. for i = 1 to n
    if activity i has no overlap w/ activities in S:
        add activity i in S
3. return S
"""
def greedy_one_activity(List):
    S = []
    sorted_list = sorted(List)
    S.append(sorted_list[0])
    last_finish = sorted_list[0][1]
    for i in range(1, len(sorted_list)):
        sj, fj = sorted_list[i]
        if sj >= last_finish:
            S.append(sorted_list[i])
            last_finish = fj

    return S

print(greedy_one_activity(a))

"""
Using a greedy algorithm #2
Steps:
1. sort in order of finish time. S = [] for optimitaly
2. for i = 1 to n
    if activity i has no overlap w/ activities in S:
        add activity i in S
3. return S
"""
def greedy_two_activity(List):
    S = []
    sorted_list = 0
    return S