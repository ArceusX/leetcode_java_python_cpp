class Solution {
    private List<Integer>[] adjList;
    private Queue<Integer> queue;

    public int[] findOrder(int n, int[][] prerequisites) {
        adjList = new ArrayList[n];
        Arrays.setAll(adjList, srcNode -> new ArrayList<>());
        queue = new LinkedList<>();

        // Can use enum, but for efficiency, remember
        // 0: unchecked; 1: in path stack; 2: visited/done
        int[] status = new int[n];

        for (int[] pre: prerequisites) {
            adjList[pre[0]].add(pre[1]);
        }

        for (int node = 0; node < n; node++) {
            if (dfsCyclic(node, status)) return new int[0];
        }
        
        return queue.stream().mapToInt(i->i).toArray();
    }
    private boolean dfsCyclic(int current, int[] status) {
        if (status[current] == 1) return true;
        if (status[current] == 2) return false;

        status[current] = 1;

        for (int toNode: adjList[current]) {
            if (dfsCyclic((int)toNode, status)) return true;
        }

        status[current] = 2;
        queue.offer(current);
        return false;
    }
}