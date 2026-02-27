from collections import defaultdict, deque
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        print("Adjacency List:")
        for vertex in range(self.V):
            print(f"{vertex} -> {self.graph[vertex]}")

    def draw_graph(self):
        G = nx.DiGraph()

        for i in range(self.V):
            G.add_node(i)
        
        for u in self.graph:
            for v in self.graph[u]:
                G.add_edge(u, v)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True,
                node_color='lightblue',
                node_size=2000,
                font_size=12,
                arrows=True)

        plt.title("Directed Acyclic Graph (DAG)")
        plt.show()

    def topological_sort(self):
        in_degree = [0] * self.V

        
        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1

        queue = deque()

    
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        topo_order = []
        count = 0

        while queue:
            u = queue.popleft()
            topo_order.append(u)

            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

            count += 1


        if count != self.V:
            print("Graph contains a cycle! Topological sort not possible.")
            return None

        return topo_order
    
g = Graph(6)


g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.print_graph()
g.draw_graph()

result = g.topological_sort()
print("Topological Order:", result)