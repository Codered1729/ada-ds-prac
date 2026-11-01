import java.util.Scanner;

public class ArticulationPointsMatrix {

    static int time = 0;

    public static void dfs(int u, int parent, int[][] graph, int V,
                           boolean[] visited, int[] disc, int[] low,
                           boolean[] isAP) {
        visited[u] = true;
        disc[u] = low[u] = ++time;
        int children = 0;

        for (int v = 0; v < V; v++) {
            if (graph[u][v] != 0) {
                if (v == parent) continue;

                if (visited[v]) {
                    low[u] = Math.min(low[u], disc[v]);
                } else {
                    children++;
                    dfs(v, u, graph, V, visited, disc, low, isAP);
                    low[u] = Math.min(low[u], low[v]);

                    if (parent != -1 && low[v] >= disc[u]) {
                        isAP[u] = true;
                    }
                }
            }
        }

        if (parent == -1 && children > 1) {
            isAP[u] = true;
        }
    }

    public static void findArticulationPoints(int[][] graph, int V) {
        boolean[] visited = new boolean[V];
        int[] disc = new int[V];
        int[] low = new int[V];
        boolean[] isAP = new boolean[V];

        time = 0;

        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                dfs(i, -1, graph, V, visited, disc, low, isAP);
            }
        }

        System.out.println("\nArticulation Points (Cut Vertices):");
        boolean found = false;
        for (int i = 0; i < V; i++) {
            if (isAP[i]) {
                System.out.println("Vertex " + i);
                found = true;
            }
        }

        if (!found) {
            System.out.println("No articulation points present in the graph.");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of vertices: ");
        int V = sc.nextInt();

        int[][] graph = new int[V][V];
        System.out.println("Enter the adjacency matrix (" + V + "x" + V + "):");
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                graph[i][j] = sc.nextInt();
            }
        }

        findArticulationPoints(graph, V);
        sc.close();
    }
}
