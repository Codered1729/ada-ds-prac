import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number of nodes");
        int n = sc.nextInt();

        int[][] graph = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                graph[i][j] = sc.nextInt();
            }
        }

        System.out.println("Enter the starting node");
        int start = sc.nextInt();

        boolean[] visited = new boolean[n];
        int[] dist = new int[n];

        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;

        for (int k = 0; k < n - 1; k++) {
            int u = -1;
            int min = Integer.MAX_VALUE;
            for (int i = 0; i < n; i++) {
                if (!visited[i] && dist[i] < min) {
                    min = dist[i];
                    u = i;
                }
            }

            if (u == -1) {
                break;
            }

            visited[u] = true;

            for (int v = 0; v < n; v++) {
                if (graph[u][v] != 0 && !visited[v]) {
                    int newdist = dist[u] + graph[u][v];

                    if (newdist < dist[v]) {
                        dist[v] = newdist;
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (i != start) {
                System.out.println(start + " -> " + i + " = "
                    + (dist[i] == Integer.MAX_VALUE ? "INF" : dist[i]));
            }
        }

        sc.close();
    }
}
