//Approach: https://leetcode.com/problems/redundant-connection-ii/discuss/108058/one-pass-disjoint-set-solution-with-explain
//Without excess edge, every non-root node has 1 inEdge and root has none.
//With excess edge, either root gains inEdge or another node now has 2.
//Consider if adding excess node creates cycle, if it points to current
//root of its set and later another node becomes root. Consider which
//of several inEdges to same node can be removed to keep tree connected.

class Solution {
public:
    
    int * parent, * edgeTo;
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        parent = new int[edges.size() + 1]();
        
        edgeTo = new int[edges.size() + 1];
        std::fill_n(edgeTo, edges.size() + 1, -1);
        
        int inEdge1 = -1, inEdge2 = -1, edgeToRoot = -1;

        for (int edge = 0; edge < edges.size(); edge++) {
            int srcNode = edges[edge][0],
                toNode = edges[edge][1];

            if (edgeTo[toNode] == -1) {

                edgeTo[toNode] = edge;
                
                int rtOfSrcNode = find(srcNode);

                if (rtOfSrcNode == toNode) {
                    edgeToRoot = edge;
                }

                else parent[toNode] = rtOfSrcNode;
            }

            else {
                inEdge1 = edgeTo[toNode];
                inEdge2 = edge;
            }
        }

        //ie:     e[[2, 3], [3, 4], [4, 5], [4, 6]
        //Case 1: if (inEdge2 == -1): +e[6, 2]. Remove e[6, 2]
        //Case 2: if (edgeToRoot == -1): +e[6, 3]. Remove e[6, 3]
        //Case 3: if (inEdge2 != -1 && inEdge2 != 1)
        //        +e[6, 2], [1, 2]. Remove e[6, 2] (inEdge1)
        //Case 3: +e[6, 2], [7, 3]. Remove e[2, 3] 

        //Case 1: else {inEdge1 = ..; inEdge2 = ..} skipped on all
        //iterations, so root is node given excess inEdge (it
        //should have 0 inEdge). Mark root's inEdge for removal
        if (inEdge2 == -1) return edges[edgeToRoot];

        //Cases 1, 2: Non-root node given excess 2nd inEdge.
        //Case 1: Remove inEdge2 because it occurs after inEdge1
        //Case 2: Except if removing inEdge2 rather than inEdge1
        //would split tree, which occurs when current root of its
        //tree gains inEdge, then any other node receives inEdge2.
        //ie: branch if (rtOfSrcNode == toNode) followed, then
        //branch else {inEdge1 = ..; inEdge2 = ..} followed

        //Case 2
        if (edgeToRoot == -1) return edges[inEdge2];

        //Case 3 
        return edges[inEdge1];
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