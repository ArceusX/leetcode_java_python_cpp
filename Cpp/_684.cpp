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
public:
    int* parent;
    
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        
        //Parent entry being 0 means root is itself (node in own set)
        parent = new int[edges.size() + 1]();
        
        for (const auto& edge : edges) {
            int root0 = find(edge[0]);
            int root1 = find(edge[1]);  
            if (root0 == root1) {
                return edge;
            }

            parent[root0] = root1;
        }
        
        return vector<int>();
    }
    
    int find(int x) {
        while (parent[x] != 0) {
            int temp = parent[x];
            if (parent[temp] != 0) parent[x] = parent[temp];
            x = temp;
        }

        return x;
    }
};