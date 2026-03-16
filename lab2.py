def topological_sort(n, edges):
    adj = [[0]*n for _ in range(n)]
    indegree = [0]*n

    for u, v in edges:
        adj[u][v] = 1
        indegree[v] += 1

    order = []

    for _ in range(n):
        for i in range(n):
            if indegree[i] == 0:
                order.append(i)
                indegree[i] = -1
                for j in range(n):
                    if adj[i][j] == 1:
                        indegree[j] -= 1
                break
        else:
            print("Cycle detected")
            return

    print("Topological Order:", order)

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
edges = []
for _ in range(e):
    u, v = map(int, input().split())
    edges.append((u, v))

topological_sort(n, edges)
