"""
You are given:
    - a list od coin denominations
    - a target amount
You must use the min # of coins to maks that amount

e.g. 
coins = [1,5,10,25]
amount = 37
Output: [25,10,1,1] #or any order
Total coins = 4
"""

def minCoins(coins,amount):
    #sorting coin denominations
    sorted_coins = sorted(coins, reverse=True)
    print(sorted_coins)
    curr = amount
    s = []
    i = 0
    while curr != 0:
        #i = 0
        if curr >= sorted_coins[i]:
            s.append(sorted_coins[i])
            #print("s: ",s)
            curr = curr - sorted_coins[i]
        else:
            i += 1
    total = len(s)
    return total, s

coins = [1, 5, 10, 25]
amount = 37

print(minCoins(coins, amount))

coins = [1, 2, 5]
amount = 11

print(minCoins(coins, amount))

"""
Woah... here i noticed greedy failing, it outputed: [4, 1, 1]
but the optimal solution is obv [3,3] 
"""
coins = [1, 3, 4]
amount = 6

print(minCoins(coins, amount))
