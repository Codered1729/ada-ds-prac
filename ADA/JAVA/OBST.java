import java.util.*;

class Main {
    static void printTree(int[][] root, int[] keys,
                          int i, int j, String prefix, String label) {
        if (i > j) {
            return;
        }

        int r = root[i][j];

        System.out.println(prefix + label + keys[r]);

        printTree(root, keys, i, r - 1,
                  prefix + "    ", "Left: ");

        printTree(root, keys, r + 1, j,
                  prefix + "    ", "Right: ");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter number of keys");
        int n = sc.nextInt();

        int[] keys = new int[n];
        int[] freq = new int[n];

        System.out.println("Enter sorted keys");
        for (int i = 0; i < n; i++) {
            keys[i] = sc.nextInt();
        }

        System.out.println("Enter search frequencies");
        for (int i = 0; i < n; i++) {
            freq[i] = sc.nextInt();
        }

        long[][] dp = new long[n][n];
        int[][] root = new int[n][n];
        long[] prefix = new long[n + 1];

        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + freq[i];
            dp[i][i] = freq[i];
            root[i][i] = i;
        }

        for (int len = 2; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;

                long sum = prefix[j + 1] - prefix[i];
                dp[i][j] = Long.MAX_VALUE;

                for (int r = i; r <= j; r++) {
                    long left = (r > i) ? dp[i][r - 1] : 0;
                    long right = (r < j) ? dp[r + 1][j] : 0;

                    long cost = left + right + sum;

                    if (cost < dp[i][j]) {
                        dp[i][j] = cost;
                        root[i][j] = r;
                    }
                }
            }
        }

        System.out.println("Minimum search cost: "
                + (n == 0 ? 0 : dp[0][n - 1]));

        if (n > 0) {
            System.out.println("OBST structure:");
            printTree(root, keys, 0, n - 1, "", "Root: ");
        }

        sc.close();
    }
}
