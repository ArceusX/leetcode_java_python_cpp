"""
Problem: Essential asks if topological sort for given directed
         graph is possible, which requires that graph be acylic.

Solve  : Kahn's algo creates valid sort if able. Indicate whether
         sort is possible. Depth-first search.
"""


class Solution:
    def canFinish(self, nu: int, prerequisites: List[List[int]]) -> bool:

        adjList = [[] for _ in range(n)]

        inDegree = [0] * n

        # 2: Record out-edges and update indegree of each node
        for toNode, srcNode in prerequisites:
            adjList[srcNode].append(toNode)
            inDegree[toNode] += 1

        # 3: Collect nodes with indegree 0 for traversal
        toVisit = [node for node in range(n) if inDegree[node] == 0]

        # 4: Visit marked. Remove outEdges of visited nodes and ...(5)
        for visited in toVisit:
            for toNode in adjList[visited]:

                # 5: if "toNode" neighbor once outEdge is removed no
                #    longer has inEdge, mark "toNode" to visit
                inDegree[toNode] -= 1
                if inDegree[toNode] == 0:
                    toVisit.append(toNode)

        # Check if able to visit every node
        return len(toVisit) == n