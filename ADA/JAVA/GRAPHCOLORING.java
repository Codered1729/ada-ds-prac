import java.util.*;

class Main {
    static int n;
    static int m;
    static int[][] graph;
    static int[] color;
    static int solutionCount = 0;

    static boolean isSafe(int vertex, int c) {
        for (int i = 0; i < n; i++) {
            if (graph[vertex][i] != 0 && color[i] == c) {
                return false;
            }
        }

        return true;
    }

    static void solve(int vertex) {
        if (vertex == n) {
            solutionCount++;

            System.out.println("Solution " + solutionCount + ": "
                    + Arrays.toString(color));
            return;
        }

        for (int c = 1; c <= m; c++) {
            if (isSafe(vertex, c)) {
                color[vertex] = c;

                solve(vertex + 1);

                color[vertex] = 0;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number of vertices");
        n = sc.nextInt();

        graph = new int[n][n];

        System.out.println("Enter adjacency matrix");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                graph[i][j] = sc.nextInt();
            }
        }

        System.out.println("Enter number of colors");
        m = sc.nextInt();

        color = new int[n];

        solve(0);

        if (solutionCount == 0) {
            System.out.println("No valid coloring exists");
        } else {
            System.out.println("Total solutions: " + solutionCount);
        }

        sc.close();
    }
}
