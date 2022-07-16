class Solution {
    List<Integer>[] adjList;

    public boolean canFinish(int n, int[][] prerequisites) {
        adjList = new ArrayList[n];
        Arrays.setAll(adjList, srcNode -> new ArrayList<>());

        // Can use enum, but for efficiency, remember
        // 0: unchecked; 1: in path stack; 2: visited/done
        int[] status = new int[n];

        for (int[] pre: prerequisites) {
            // prereqs given as 0 <- 1 (1 is 0's prereq)
            adjList[pre[0]].add(pre[1]);
        }

        for (int node = 0; node < n; node++) {
            if (dfsCyclic(node, status)) return false;
        }

        return true;
    }
    private boolean dfsCyclic(int current, int[] status) {
        if (status[current] == 1) return true;
        if (status[current] == 2) return false;

        status[current] = 1;

        for (int toNode: adjList[current]) {
            if (dfsCyclic((int)toNode, status)) return true;
        }

        status[current] = 2;
        return false;
    }
}