class Solution {
    int n;
    int[][] weight;
    int threshold;
    List<Integer>[] adjList;
    public int findTheCity(int n, int[][] edges, int threshold) {
        this.n = n;
        this.threshold = threshold;
        weight = new int[n][n];
        for (int[] row: weight) Arrays.fill(row, Integer.MAX_VALUE);
        adjList = new ArrayList[n];
        
        for (int i = 0; i < n; i++) {
            adjList[i] = new ArrayList<>();
        }
        
        for (int[] edge : edges) {
            weight[edge[0]][edge[1]] = weight[edge[1]][edge[0]] = edge[2];
            adjList[edge[0]].add(edge[1]);
            adjList[edge[1]].add(edge[0]);
        }

        int[] nInThreshold = new int[n];
        for (int i = 0; i < n; i++) {
            nInThreshold[i] = dijkstra(i);
        }

        return IntStream.range(0, nInThreshold.length)
            .reduce((a, b) -> nInThreshold[a] < nInThreshold[b] ? a : b)
            .getAsInt();
    }
    
    public int dijkstra(int root) {
        int[] minCost = new int[n];
        Arrays.fill(minCost, Integer.MAX_VALUE);
        minCost[root] = 0;
        
        PriorityQueue<int[]> heap = new PriorityQueue<>((a,b) -> Integer.compare(a[0],b[0]));
        heap.add(new int[] {0, root});
        
        while (!heap.isEmpty()) {
            int[] costNNode = heap.poll();
            int cost = costNNode[0], node = costNNode[1];
            if (minCost[node] < cost) continue;
            
            for (int nbor : adjList[node]) {
                int pathCost = costNNode[0] + weight[node][nbor];
                
                if (pathCost < minCost[nbor]) {
                    minCost[nbor] = pathCost;
                    heap.add(new int[] {pathCost, nbor});
                }
            }
        }
        return (int) Arrays.stream(minCost).filter(i-> i <= threshold).count();                    
    }
}