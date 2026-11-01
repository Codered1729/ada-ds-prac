import java.util.Scanner;

public class OptimalBST {

    public static void computeOBST(double[] p, double[] q, int n) {
        // Tables are of size (n + 2) x (n + 1) to handle 0-based boundary conditions
        double[][] c = new double[n + 2][n + 1];
        double[][] w = new double[n + 2][n + 1];
        int[][] r = new int[n + 2][n + 1];

        // 1. Base cases: trees with 0 keys (only dummy key q[i])
        for (int i = 0; i <= n; i++) {
            w[i][i] = q[i];
            c[i][i] = 0;
        }

        // 2. l is the chain length (number of keys in the subproblem, from 1 to n)
        for (int l = 1; l <= n; l++) {
            for (int i = 0; i <= n - l; i++) {
                int j = i + l;

                // Weight formula: sum of probabilities in range
                w[i][j] = w[i][j - 1] + p[j] + q[j];
                c[i][j] = Double.MAX_VALUE;

                // 3. Try each key r as the root of the subtree
                for (int root = i + 1; root <= j; root++) {
                    double cost = c[i][root - 1] + c[root][j] + w[i][j];

                    // Greedily pick the minimum search cost
                    if (cost < c[i][j]) {
                        c[i][j] = cost;
                        r[i][j] = root; // Store the root index
                    }
                }
            }
        }

        // 4. Print results
        System.out.printf("\nOptimal Search Cost: %.4f\n", c[0][n]);
        System.out.println("Root of the Optimal BST: Key " + r[0][n]);

        // Print Root Table for reference in the lab record
        System.out.println("\nRoot Table r[i][j]:");
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                if (j >= i + 1) {
                    System.out.printf("%4d", r[i][j]);
                } else {
                    System.out.print("   -");
                }
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of keys (n): ");
        int n = sc.nextInt();

        // p has indices 1 to n
        double[] p = new double[n + 1];
        System.out.println("Enter probabilities for successful searches p[1] to p[" + n + "]:");
        for (int i = 1; i <= n; i++) {
            p[i] = sc.nextDouble();
        }

        // q has indices 0 to n
        double[] q = new double[n + 1];
        System.out.println("Enter probabilities for unsuccessful searches q[0] to q[" + n + "]:");
        for (int i = 0; i <= n; i++) {
            q[i] = sc.nextDouble();
        }

        computeOBST(p, q, n);
        sc.close();
    }
}