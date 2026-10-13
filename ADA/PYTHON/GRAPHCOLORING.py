def issafe(vertex, c, n, graph, color):
    for i in range(n):
        if graph[vertex][i] != 0 and color[i] == c:
            return False
    return True


solutioncount = 0

def solve(vertex, n, m, graph, color):
    global solutioncount
    if vertex == n:
        solutioncount += 1
        print("Solution " + str(solutioncount) + ":", color)
        return

    for c in range(1, m + 1):
        if issafe(vertex, c, n, graph, color):
            color[vertex] = c
            solve(vertex + 1, n, m, graph, color)
            color[vertex] = 0


n = int(input("Enter number of vertices\n"))
print("Enter adjacency matrix")
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

m = int(input("Enter number of colors\n"))
color = [0] * n

solve(0, n, m, graph, color)

if solutioncount == 0:
    print("No valid coloring exists")
else:
    print("Total solutions:", solutioncount)

