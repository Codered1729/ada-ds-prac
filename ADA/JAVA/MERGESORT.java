import java.util.*;

class Main {
    static void merge(int[] a, int left, int mid, int right) {
        int n = right - left + 1;
        int[] temp = new int[n];
        int i = left, j = mid + 1, k = 0;

        while (i <= mid && j <= right) {
            if (a[i] <= a[j]) {
                temp[k] = a[i];
                i++;
            } else {
                temp[k] = a[j];
                j++;
            }
            k++;
        }   

        while (i <= mid) {
            temp[k] = a[i];
            i++;
            k++;
        }

        while (j <= right) {
            temp[k] = a[j];
            j++;
            k++;
        }

        for ( i = 0; i < n; i++) {
            a[left + i] = temp[i];
        }
    }

    static void mergeSort(int[] a, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            mergeSort(a, mid + 1, right);
            mergeSort(a, left, mid);
            merge(a, left, mid, right);
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
        mergeSort(a, 0, n - 1);
        for (int i : a) {
            System.out.print(i + " ");
        }
    }
}