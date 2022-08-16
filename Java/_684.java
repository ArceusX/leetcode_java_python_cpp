/*
Algo: For minimum spanning tree, each edge added during
      its construction connects 2 nodes not already
      reachable via intermediates in same set. Edge that
      connects two already reachable nodes ruins MST.
      With disjoint union set, label reachable nodes as
      belong to same set; if another edge connects 2 nodes
      already in same set/reachable, new edge is excess.
*/

class Solution {

    int[] parent;
    public int[] findRedundantConnection(int[][] edges) {
        
        // For MST, # nodes == # edges + 1; 1st edge adds 
        // 2 new nodes; each edge afterward connects 1 
        // already added and 1 new, so 1 new. parent[0]
        // unused because nodes given as 1 to n
        // 0 for parent val means node is its own root
        parent = new int[edges.length + 1];

        for (int[] edge : edges) {

            // If checked nodes have same root, nodes already
            // belong to same set and new edge is excess.
            int root0 = find(edge[0]);
            int root1 = find(edge[1]);  

            if (root0 == root1) return edge;

            // If different sets, merge sets by setting
            // root of one set to point to other root
            parent[root0] = root1;
        }

        return new int[2];
    }

    int find(int x) {

        // Iterate until reach root. Along way, compress path
        while (parent[x] != 0) {
            int temp = parent[x];
            if (parent[temp] != 0) parent[x] = parent[temp];
            x = temp;
        }

        return x;
    }
}