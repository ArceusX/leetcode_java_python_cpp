// See 207.java. With 210.java, return sort (toVisit) list rather than
// indicate if it exists or not. If it doesn't, return empty.

class Solution {
    public int[] findOrder(int n, int[][] prerequisites) {

        ArrayList<Integer>[] adjList = new ArrayList[n];
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

        if (toVisit.size() == n) return toVisit.stream().mapToInt(i->i).toArray();
        else return new int[0];
    }
}