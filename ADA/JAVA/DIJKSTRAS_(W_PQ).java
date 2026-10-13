import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter number of nodes");
        int n = sc.nextInt();
        int[][] graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                graph[i][j] = sc.nextInt();
            }
        }

        System.out.println("enter the starting node");
        int start = sc.nextInt();

        boolean[] visited = new boolean[n];
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> Integer.compare(a[0], b[0])
        );
        pq.offer(new int[]{0, start});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int d = cur[0];
            int u = cur[1];

            if (visited[u]) {
                continue;
            }
            visited[u] = true;

            for (int v = 0; v < n; v++) {
                if (graph[u][v] != 0 && !visited[v]) {
                    int newdist = d + graph[u][v];
                    if (newdist < dist[v]) {
                        dist[v] = newdist;
                        pq.offer(new int[]{newdist, v});
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