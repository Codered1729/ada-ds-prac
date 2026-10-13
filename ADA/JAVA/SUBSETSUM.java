import java.util.*;

class Main {
    static void SubsetSum(int[] arr, int n, int sum, int[] sol) {
        if (sum == 0) {
            System.out.println(Arrays.toString(sol));
            return;
        }

        if (n == 0 || sum < 0)
            return;

        sol[n - 1] = 1;

        SubsetSum(arr, n - 1, sum - arr[n - 1], sol);

        sol[n - 1] = 0;

        SubsetSum(arr, n - 1, sum, sol);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        System.out.println("Enter array elements:");

        int[] arr = new int[n];

        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        System.out.println("Enter Sum(k):");

        int k = sc.nextInt();

        int[] sol = new int[n];

        SubsetSum(arr, n, k, sol);

        sc.close();
    }
}
