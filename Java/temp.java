//Approach from https://leetcode.com/problems/redundant-connection-ii/discuss/108058/one-pass-disjoint-set-solution-with-explain

//Use disjoint union set to record which nodes are reachable from
//some other node via intermediates. Remember known info (tree 
//spans all nodes; without excess edge, all nodes have exactly 1 
//inEdge, except for root, which has none). Consider cases and 
//which node can be removed within violating tree guarantee

class Solution {
    
    int[] parent;
    int[] edgeTo;
    public int[] findRedundantDirectedConnection(int[][] edges) {

        //parent[node1] == node2 means node1 reachable from node2
        //node2 typically being current root of its llocal set
        parent = new int[edges.length + 1];

        //Index in edges of inEdge to node, or -1 if it has none
        edgeTo = new int[edges.length + 1];
        Arrays.fill(edgeTo, -1);

        //If 2 edges point to same node, mark them as inEdge1|2
        //(!= 1) If can remove either, remove edge added later
        int inEdge1 = -1, inEdge2 = -1, edgeToRoot = -1;

        for (int edge = 0; edge < edges.length; edge++) {
            int fromNode = edges[edge][0],
                toNode = edges[edge][1];

            //If toNode hasn't had edge pointing to it yet
            if (edgeTo[toNode] == -1) {

                //Record index of edge pointing to toNode
                edgeTo[toNode] = edge;
                
                //Root of set fromNode currently belongs in
                int rtOfFromNode = find(fromNode);

                //If toNode has no inEdge yet, it is either current
                //root of fromNode's set (if..) or node from
                //different set (else..) (Otherwise, for toNode to
                //not be root of its set, 
                // toNode would already have inEdge, contradicting
                //assumption if (edgeTo[toNode] == -1)

                if (rtOfFromNode == toNode) {
                    edgeToRoot = edge;
                }

                //Mark rtOfFromNode is now root of toNode
                //through fromNode (rtOfFromNode is root of set
                //toNode just joined)
                else parent[toNode] = rtOfFromNode;
            }

            //Edge points to non-root node already with inEdge
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
        //ie: branch if (rtOfFromNode == toNode) followed, then
        //branch else {inEdge1 = ..; inEdge2 = ..} followed

        //Case 2
        if (edgeToRoot == -1) return edges[inEdge2];

        //Case 3 
        return edges[inEdge1];
    }
    
    public int find(int x) {
        while (parent[x] != 0) {
            int temp = parent[x];
            parent[x] = parent[temp];
            x = temp;
        }

        return x;
    }
}