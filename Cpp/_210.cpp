/* 207.cpp asks for indicator if sort can be found. 210.cpp asks for
 * any valid sort itself. Use Kahn's algo.
 */

class Solution {
    public:
    // prereqs is vector of edges of [a, b] in which a <- b
    // (b must complete before a; edge[0] <- edge[1])
    vector<int> findOrder(int n, vector<vector<int>>& prerequisites) {

        vector<vector<int>> adjList(n);

        // 1: Initialize toVisit list to empty. Kahn's algo 
        //    checks if sort is possible by checking if count of
        //    of visited nodes by end is all of them
        vector<int> inDegree(n, 0), toVisit;

        // 2: Record out-edges and indegree of each node (0 <- 1)
        for (auto& edge : prerequisites) {

            // edge[1] has edge[0] node as outNode 
            adjList[edge[1]].push_back(edge[0]);
            inDegree[edge[0]]++;
        }

        // 3: Collect nodes with indegree 0 before any edge is removed
        //    and graph simplified. These have no other node required
        //    to precede them in sort and will be visited first
        for (int visited = 0; visited < n; ++visited) {
            if (inDegree[visited] == 0) {
                toVisit.push_back(visited);
            }
        }

        // 4: Visit marked. Remove outEdges of visited nodes and ..(5)
        for (int visited = 0; visited < toVisit.size(); ++visited) {
            for (int outEdge: adjList[toVisit[visited]]) {

                // 5: if "toNode" neighbor once outEdge is removed no
                //    longer has inEdge, mark "toNode" to visit.
                if (--inDegree[outEdge] == 0) {
                    toVisit.push_back(outEdge);
                }
            }
        }

        // For Step 3|5: If at any point, there is no longer any node
        // of indegree 0, acylic path from node of indegree 0 to visit 
        // remaining nodes not possible and thus sort not possible
        return (toVisit.size() == n) ? toVisit : vector<int>();
    }
};