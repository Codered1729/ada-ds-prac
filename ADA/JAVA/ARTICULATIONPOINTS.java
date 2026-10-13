import java.util.*;

class Main {
    static int time = 0;

    static void DFS(int u, int parent, int[][] graph,
                    int[] dfn, int[] l, boolean[] ap) {
        dfn[u] = l[u] = ++time;
        int children = 0;

        for (int w = 0; w < graph.length; w++) {
            if (graph[u][w] == 1) {
                if (dfn[w] == 0) {
                    children++;

                    DFS(w, u, graph, dfn, l, ap);

                    l[u] = Math.min(l[u], l[w]);

                    if (parent != -1 && l[w] >= dfn[u]) {
                        ap[u] = true;
                    }
                } else if (w != parent) {
                    l[u] = Math.min(l[u], dfn[w]);
                }
            }
        }

        if (parent == -1 && children > 1) {
            ap[u] = true;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[][] graph = new int[n][n];

        System.out.println("Enter adjacency matrix of a graph");

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                graph[i][j] = sc.nextInt();
            }
        }

        int[] dfn = new int[n];
        int[] l = new int[n];
        boolean[] ap = new boolean[n];

        for (int u = 0; u < n; u++) {
            if (dfn[u] == 0) {
                DFS(u, -1, graph, dfn, l, ap);
            }
        }

        System.out.println("Articulation points are:");

        for (int u = 0; u < n; u++) {
            if (ap[u]) {
                System.out.print(u + " ");
            }
        }

        System.out.println();
        sc.close();
    }
}
