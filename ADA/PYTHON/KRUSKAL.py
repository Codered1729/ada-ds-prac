n = int(input("Enter number of nodes\n"))
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

edges = []
for i in range(n):
    for j in range(i + 1, n):
        if graph[i][j] != 0:
            edges.append([graph[i][j], i, j])

edges.sort(key=lambda x: x[0])

parent = list(range(n))
totalcost = 0
count = 0

print("Edges in MST are")

for wt, u, v in edges:
    a = u
    b = v
    while parent[a] != a:
        a = parent[a]
    while parent[b] != b:
        b = parent[b]

    if a != b:
        print(f"{u}->{v}:{wt}")
        parent[a] = b
        totalcost += wt
        count += 1

    if count == n - 1:
        break

if count == n - 1:
    print("total cost :", totalcost)
else:
    print("MST cant be formed")

