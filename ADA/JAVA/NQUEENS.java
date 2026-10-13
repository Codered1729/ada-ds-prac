import java.util.*;

class Main {
    static int n;
    static int[] x;

    static boolean place(int k, int i) {
        for (int j = 1; j < k; j++) {
            if (x[j] == i)
                return false;

            if (Math.abs(x[j] - i) == Math.abs(j - k))
                return false;
        }

        return true;
    }

    static void n_queen(int k) {
        for (int i = 1; i <= n; i++) {
            if (place(k, i)) {
                x[k] = i;

                if (k == n) {
                    for (int j = 1; j <= n; j++) {
                        System.out.print(x[j] + " ");
                    }

                    System.out.println();
                } else {
                    n_queen(k + 1);
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter n: ");
        n = sc.nextInt();

        if (n < 4) {
            System.out.println("-1");
            sc.close();
            return;
        }

        x = new int[n + 1];

        System.out.println("The possible ways are:");
        n_queen(1);

        sc.close();
    }
}
