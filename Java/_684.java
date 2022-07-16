/*
Approach: For minimum spanning tree, each edge added during
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
        
        //For minimum spanning tree, # nodes == # edges + 1
        //1st edge adds 2 new nodes; each edge thereafter
        //connects 1 already added and 1 new, so 1 new.
        //Nodes given as 1 to n; parent[0] unused
        //Parent entry being 0 means root is itself (node in own set)
        parent = new int[edges.length + 1];

        for (int[] edge : edges) {

            //Find root of each checked node. If their roots
            //are same, they already belong to same set and
            //thus new edge is excess.
            int root0 = find(edge[0]);
            int root1 = find(edge[1]);  

            if (root0 == root1) {
                return edge;
            }

            //Otherwise, merge sets containing checked nodes
            //by making root of one set point to other
            parent[root0] = root1;
        }

        return new int[2];
    }

    int find(int x) {

        //Iterate until get to root. Along way, compress path
        while (parent[x] != 0) {
            int temp = parent[x];
            if (parent[temp] != 0) parent[x] = parent[temp];
            x = temp;
        }

        return x;
    }
}