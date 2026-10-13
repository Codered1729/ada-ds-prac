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

        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (graph[i][j] != 0) {
                    edges.add(new int[]{graph[i][j], i, j});
                }
            }
        }

        edges.sort((a, b) -> Integer.compare(a[0], b[0]));

        int[] parent = new int[n];

        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        int totalcost = 0;
        int count = 0;

        System.out.println("Edges in MST are");

        for (int[] edge : edges) {
            int wt = edge[0];
            int u = edge[1];
            int v = edge[2];

            int a = u;
            int b = v;
            while (parent[a] != a) {
                a = parent[a];
            }
            while (parent[b] != b) {
                b = parent[b];
            }

            if (a != b) {
                System.out.println(u + "->" + v + ":" + wt);
                parent[a] = b;
                totalcost += wt;
                count++;
            }
            if (count == n - 1) {
                break;
            }
        }
        if (count == n - 1) {
            System.out.println("total cost :" + totalcost);
        } else {
            System.out.println("MST cant be formed");
        }

        sc.close();
    }
}
