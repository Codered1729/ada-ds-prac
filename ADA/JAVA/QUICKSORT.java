import java.util.*;

class Main {
    static int partition(int[] a, int left, int right) {
        int i = left - 1;
        int pivot = a[right];

        for (int j = left; j < right; j++) {
            if (a[j] < pivot) {
                i++;
                int temp = a[j];
                a[j] = a[i];
                a[i] = temp;
            }
        }
        i++;
        int temp = a[i];
        a[i] = pivot;
        a[right] = temp;
        return i;
    }

    static void quickSort(int[] a, int left, int right) {
        if (left < right) {
            int pivot = partition(a, left, right);
            quickSort(a, left, pivot - 1);
            quickSort(a, pivot + 1, right);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the number of elements");
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        quickSort(a, 0, n - 1);

        for (int i : a) {
            System.out.print(i + " ");
        }
    }
}