from graph import Graph
from collections import deque

def bfs(graph, s):
    Q = deque()
    
    # Step 1: initialize distances
    dist = {}
    for u in graph.get_vertices():
        dist[u] = float('inf')
    print(dist)

    dist[s] = 0
    Q.append(s)

    # Step 2: BFS loop
    while Q:
        u = Q.popleft()

        for v in graph.get_neighbors(u):
            if dist[v] == float('inf'):
                Q.append(v)
                print(f"Q: {Q}")
                dist[v] = dist[u] + 1

    return dist

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')

print(bfs(g, 'A'))