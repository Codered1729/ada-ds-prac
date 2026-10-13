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
        boolean[] visited = new boolean[n];
        int[] key = new int[n];
        int[] parent = new int[n];

        Arrays.fill(key, Integer.MAX_VALUE);
        Arrays.fill(parent, -1);

        key[0]= 0;
        int totalcost = 0;
        System.out.println("the edges in the MST are ");

        for(int k = 0; k < n ; k++){
            int u = -1;
            int min = Integer.MAX_VALUE;
            for(int i = 0; i < n; i++){
                if(!visited[i] && key[i] < min){
                    min = key[i];
                    u = i;
                }
            }
            if( u == -1 ){
                break;
            } 
            visited[u] = true;
            if(parent[u] != -1){
                System.out.println(parent[u] + " -> " + u+ " : " + graph[parent[u]][u]);
                totalcost += graph[parent[u]][u];
            }

            for(int v= 0 ; v < n ; v++){
                if(graph[u][v] != 0 && !visited[v] && graph[u][v] < key[v]){
                    key[v] = graph[u][v];
                    parent[v] = u;
                }
            }
        }
        System.out.println("the total cost of MST = "+ totalcost);
    }
}
