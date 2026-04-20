"""
Input:
    n items w/ eight w1,w2,... wn & values v1,v2,...vn
    a knapsack w/ cpacity W (total weight of items at most W)
    items are divisbile

Output:
    maximize: p1v1 + p2v2 + ... + pnvn
    contraint: p1w1 + p2w2 + .....+ pnwn <= W

where pi = fraction of item i such that pn wn <= W 
"""
from fractions import Fraction

def greedy_knapsack(l, W):
    """
    Sort items in decreasing order of vi / w2
    optimal solution.
    """
    sorted_l = sorted(l, key=lambda item: item[1] / item[0], reverse=True)
    print(sorted_l)
    total_value = 0
    fractions = []
    
    for item in sorted_l:
        w,v = item
        if W >= w:
            W -= w
            total_value += v
            fractions.append(1)
        else:
            f = Fraction(W, w)
            fractions.append(f"{f}")
            total_value += (W/w) * v
            break

    print(fractions)

    return total_value

#TEST CASES: 
W = 50
items = [(10,60), (20,100), (30,120)]

print(greedy_knapsack(items, W))

W = 60
items = [(10,20), (20,100), (30,120), (40,160)]

print(greedy_knapsack(items, W))

W = 10
items = [(5,10), (4,40), (6,30)]

print(greedy_knapsack(items, W))

W = 50
items = [(25,100), (10,60), (20,100)]
print(greedy_knapsack(items, W))