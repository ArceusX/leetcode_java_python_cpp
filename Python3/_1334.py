# Dijkstra's uses same procedure as Prim's except while Prim's calculates
# cost of new node as marginal/additional cost from intermediate already 
# calculated, Dijkstra calculates cost as total cost from root itself. 
# Prim's calculates combined cost of nodes as tree, while Dijkstra's 
# calculates cost individually as own path

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:

        # inf entry represents no direct edge between two nodes
        weight = [[float('inf')] * n for _ in range(n)]
        
        # Stores list of nbors as val for each node
        adjList = collections.defaultdict(list)
        
        # Stores weight of direct edge between two nodes
        for (a, b, c) in edges:
            weight[a][b] = weight[b][a] = c
            adjList[a].append(b)
            adjList[b].append(a)
            
        def dijkstra(root):
            minCost = [float('inf')] * n
            minCost[root] = 0

            # heap stores cost to node through intermediate to which
            # root is connected (path is not necessarily shortest)

            # cost must be 0th index for heap to sort along cost
            heap = [(0, root)]

            while heap:
                cost, node = heapq.heappop(heap)

                # Dikstra gets greedy. Wants cost of this path to be
                # lower than any other path to that same node
                if minCost[node] < cost: continue

                for nbor in adjList[node]:
                    # cost(root to nbor through node) = 
                    # minCost(root to node, current) + weight(node to nbor)
                    pathCost = cost + weight[node][nbor]

                    # Lower cost along this path than any prev calculated
                    if pathCost < minCost[nbor]:
                        minCost[nbor] = pathCost
                        heapq.heappush(heap, (pathCost, nbor))

            # -1 because each node should exclude itself as nbor
            return sum(cost <= threshold for cost in minCost) - 1
        
        # Iterate backward because in case of tie, want higher index
        nInThreshold = {i : dijkstra(i) for i in range(n - 1, -1, -1)}
        return min(nInThreshold, key = nInThreshold.get)