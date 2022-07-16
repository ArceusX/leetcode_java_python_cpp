// Depth-first search via Kahn's algo

class Solution {
    public boolean canFinish(int n, int[][] prerequisites) {

        List<Integer>[] adjList = new ArrayList[n];
        for (int node = 0; node < n; ++node) {
        	adjList[node] = new ArrayList<Integer>();
        }

        int[] inDegree = new int[n];

        for (int[] edge : prerequisites) {
            adjList[edge[1]].add(edge[0]);
            inDegree[edge[0]]++;
        }

        ArrayList<Integer> toVisit = new ArrayList();
        for (int node = 0; node < n; ++node) {
        	if (inDegree[node] == 0) {
        		toVisit.add(node);
        	}
        }

        for (int visited = 0; visited < toVisit.size(); ++visited) {
            for (int toNode: adjList[toVisit.get(visited)]) {
                if (--inDegree[toNode] == 0) {
                	toVisit.add(toNode);
                }
            }
        }

        return toVisit.size() == n;
    }
}