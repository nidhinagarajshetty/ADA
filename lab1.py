class Graph:
    def __init__(self):
        self.edges = []
        self.vertices = set()

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))
        self.vertices.add(u)
        self.vertices.add(v)

    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent, x, y):
        parent[x] = y

    def kruskal(self):
        self.edges.sort()

        parent = {v: v for v in self.vertices}
        mst = []
        cost = 0

        for w, u, v in self.edges:
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                mst.append((u, v, w))
                cost += w
                self.union(parent, x, y)

        print("\nEdges in Minimum Cost Spanning Tree:")
        for u, v, w in mst:
            print(f"{u}-{v}={w}")

        print("Total cost of MST=", cost)


# Driver Code
g = Graph()

e = int(input("Enter number of edges: "))
print("Enter edges in format: ab 3")

for _ in range(e):
    edge, w = input().split()
    g.add_edge(edge[0], edge[1], int(w))

g.kruskal()