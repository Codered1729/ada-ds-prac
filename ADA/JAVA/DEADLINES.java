import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the number of jobs");
        int n = sc.nextInt();

        int[] jobs = new int[n];
        int[] deadlines = new int[n];
        int[] profits = new int[n];

        int maxDeadline = 0;
        System.out.println("enter job id, deadline, and profit for each job:");
        for (int i = 0; i < n; i++) {
            jobs[i] = sc.nextInt();
            deadlines[i] = sc.nextInt();
            profits[i] = sc.nextInt();
            if (deadlines[i] > maxDeadline) {
                maxDeadline = deadlines[i];
            }
        }

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (profits[j] < profits[j + 1]) {
                    int tempP = profits[j];
                    profits[j] = profits[j + 1];
                    profits[j + 1] = tempP;

                    int tempD = deadlines[j];
                    deadlines[j] = deadlines[j + 1];
                    deadlines[j + 1] = tempD;

                    int tempJ = jobs[j];
                    jobs[j] = jobs[j + 1];
                    jobs[j + 1] = tempJ;
                }
            }
        }

        int[] slot = new int[maxDeadline + 1];
        Arrays.fill(slot, -1);

        int totalProfit = 0;

        for (int i = 0; i < n; i++) {
            for (int j = deadlines[i]; j > 0; j--) {
                if (slot[j] == -1) {
                    slot[j] = jobs[i];
                    totalProfit += profits[i];
                    break;
                }
            }
        }

        System.out.println("Selected Jobs:");
        for (int j = 1; j <= maxDeadline; j++) {
            if (slot[j] != -1) {
                System.out.print(slot[j] + " ");
            }
        }
        System.out.println();
        System.out.println("Total Profit: " + totalProfit);
        sc.close();
    }
}
