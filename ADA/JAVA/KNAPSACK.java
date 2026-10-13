import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter number of items: ");
        int n = sc.nextInt();
        int[] weight = new int[n];
        int[] profit = new int[n];
        double[] ratio = new double[n];
        for (int i = 0; i < n; i++) {
            System.out.println("enter item " + (i + 1) + " weight and profit");
            weight[i] = sc.nextInt();
            profit[i] = sc.nextInt();
            ratio[i] = (double) profit[i] / weight[i];
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (ratio[j] > ratio[i]) {
                    double temp = ratio[j];
                    ratio[j] = ratio[i];
                    ratio[i] = temp;
                    
                    int temp1 = weight[j];
                    weight[j] = weight[i];
                    weight[i] = temp1;

                    temp1 = profit[j];
                    profit[j] = profit[i];
                    profit[i] = temp1;
                }
            }
        }

        System.out.println("enter max capacity");
        int capacity = sc.nextInt();
        double maxprofit = 0;
        int i = 0;
        while (capacity > 0 && i < n) {
            if (weight[i] <= capacity) {
                capacity -= weight[i];
                maxprofit += profit[i];
            } else {
                double take = capacity * ratio[i];
                maxprofit += take;
                capacity = 0;
            }
            i++;
        }
        System.out.println("maxprofit : " + maxprofit);
    }
}
