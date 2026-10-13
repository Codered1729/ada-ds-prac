n = int(input("Enter number of nodes\n"))
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [False] * n
key = [float('inf')] * n
parent = [-1] * n

key[0] = 0
totalcost = 0
print("the edges in the MST are")

for k in range(n):
    u = -1
    minkey = float('inf')
    for i in range(n):
        if not visited[i] and key[i] < minkey:
            minkey = key[i]
            u = i

    if u == -1:
        break

    visited[u] = True

    if parent[u] != -1:
        print(f"{parent[u]} -> {u} : {graph[parent[u]][u]}")
        totalcost += graph[parent[u]][u]

    for v in range(n):
        if graph[u][v] != 0 and not visited[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u

print("the total cost of MST =", totalcost)

