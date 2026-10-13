timer = 0

def dfs(u, parent, graph, dfn, l, ap):
    global timer
    timer += 1
    dfn[u] = l[u] = timer
    children = 0

    for w in range(len(graph)):
        if graph[u][w] == 1:
            if dfn[w] == 0:
                children += 1
                dfs(w, u, graph, dfn, l, ap)
                l[u] = min(l[u], l[w])

                if parent != -1 and l[w] >= dfn[u]:
                    ap[u] = True
            elif w != parent:
                l[u] = min(l[u], dfn[w])

    if parent == -1 and children > 1:
        ap[u] = True


n = int(input("Enter number of nodes\n"))
print("Enter adjacency matrix of a graph")
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dfn = [0] * n
l = [0] * n
ap = [False] * n

for u in range(n):
    if dfn[u] == 0:
        dfs(u, -1, graph, dfn, l, ap)

print("Articulation points are:")
for u in range(n):
    if ap[u]:
        print(u, end=" ")
print()

