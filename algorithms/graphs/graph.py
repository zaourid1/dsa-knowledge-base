class Graph:
    def __init__(self):
        # dictionary: node -> list of neighbors
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        # for undirected graph
        if u not in self.adj:
            self.add_vertex(u)
        if v not in self.adj:
            self.add_vertex(v)

        self.adj[u].append(v)
        self.adj[v].append(u)

    def get_neighbors(self, u):
        return self.adj[u]

    def get_vertices(self):
        return list(self.adj.keys())