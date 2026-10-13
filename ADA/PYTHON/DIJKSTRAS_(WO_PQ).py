n = int(input("Enter number of nodes\n"))
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

start = int(input("Enter the starting node\n"))

visited = [False] * n
dist = [float('inf')] * n
dist[start] = 0

for k in range(n - 1):
    u = -1
    mindist = float('inf')
    for i in range(n):
        if not visited[i] and dist[i] < mindist:
            mindist = dist[i]
            u = i

    if u == -1:
        break

    visited[u] = True

    for v in range(n):
        if graph[u][v] != 0 and not visited[v]:
            newdist = dist[u] + graph[u][v]
            if newdist < dist[v]:
                dist[v] = newdist

for i in range(n):
    if i != start:
        result = "INF" if dist[i] == float('inf') else dist[i]
        print(f"{start} -> {i} = {result}")

