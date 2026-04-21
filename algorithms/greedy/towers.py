"""
Suppose you have n houses on a road. Each house postion specified by distance from left endpoint.
Positions given in P[1,2,...n]
where P[i] = x, denotes dist from end to house
Towers can cover houses that are at most R from the tower.
Goal: find min # of towers

e.g.
P = [1,5,10,15]
R = 2
expcted output: 3 towers (postion 3, 8, 13 work)

houses covered are in p [t-r,t+r]

"""

def towers(pos,r):
    sorted_pos = sorted(pos)
    l = []
    for p in sorted_pos:
        l.append((p - r, p + r))
    
    t = len(sorted_pos)

    for i in range(len(l)):
        p1,p2 = l[i]
        for j in range(i,len(l)):
            p3,p4 = l[j]
            if p2 == p3:
                t -= 1
    print(l)
    print(t)
    return 

p = [1,5,10,15]
r = 2

#print(towers(p,r))

P = [10, 1, 7, 3, 20]
R = 2
print(towers(P,R))

P = [1, 10, 20, 30]
R = 1
#print(towers(P,R))