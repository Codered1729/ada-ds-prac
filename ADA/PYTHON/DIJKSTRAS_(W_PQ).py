import heapq

n = int(input("enter number of nodes\n"))
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

start = int(input("enter the starting node\n"))

visited = [False] * n
dist = [float('inf')] * n
dist[start] = 0

pq = []
heapq.heappush(pq, (0, start))

while pq:
    d, u = heapq.heappop(pq)

    if visited[u]:
        continue
    visited[u] = True

    for v in range(n):
        if graph[u][v] != 0 and not visited[v]:
            newdist = d + graph[u][v]
            if newdist < dist[v]:
                dist[v] = newdist
                heapq.heappush(pq, (newdist, v))

for i in range(n):
    if i != start:
        result = "INF" if dist[i] == float('inf') else dist[i]
        print(f"{start} -> {i} = {result}")

