# 1584 Min Cost to Connect All Points (Prim's Algo)

# Into initially-empty connected component (CC), Prim adds
# each node via lighest edge to unadded node from any node 
# already in CC (that edge's weight as unadded node's cost)

#

# Prim 1: Track each edge in heap. Get lighest edge from heap,
#         then check if that edge connects to unadded node
# Complex.: O(nEdges * ln(nNodes))
class Solution: # Prim 1
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        isAdded = [False] * n
        
        sumCost = 0
        nInMST  = 0

        # Store [0: weight] to [1: node]. Heap to sort by [0]
        # Assign points[0] as source node with cost 0
        heap = [(0, 0)]
        
        # To iterate over edges gives no guarantee each
        # iteration adds 1 node to connected component
        while nInMST < n:
            weight, toNode = heapq.heappop(heap)
            
            # Skip already added candidate
            if isAdded[toNode]: continue
            
            # Lighest newly-scanned edge connects unadded node 
            isAdded[toNode] = True
            nInMST  += 1
            sumCost += weight

            # Push edge from newly-added node to each unadded node into heap 
            for nbor in range(n):
                if isAdded[nbor]: continue

                addCost = abs(points[toNode][0] - points[nbor][0]) +\
                abs(points[toNode][1] - points[nbor][1])
                    
                heapq.heappush(heap, (addCost, nbor))
                    
        return sumCost

#

# Prim 2: Does not use heap. Evaluates cost of each edge to
#         particular node, but track only minCost edge's weight
#         and not any specific edge, unlike Prim 1
# Complex.: O(nNodes^2). Lower than Prim 1's as in this problem,
#           each node pair is connected by edge so nEdges = nNodes^2
           
class Solution: # Prim 2
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        sumCost = 0
        
        isAdded = [False] * n
        costs   = [float('inf')] * n

        # points[0], assigned cost 0, to be first node added 
        costs[0] = 0

        # Each iteration, add unadded node (toAdd) with lowest
        # addCost, then evaluate toAdd's effect on other nodes' cost
        for nInMST in range(0, n):
            toAdd = None
            minCost = float('inf')
            for cand in range(0, n):
                if not isAdded[cand] and costs[cand] < minCost:
                    minCost = costs[cand]
                    toAdd = cand
            
            isAdded[toAdd] = True
            sumCost += minCost

            # If weight from toAdd to unadded nbor < that nbr's cost,
            # update nbr's cost (ie lighest path to nbr goes thru toAdd)
            for nbor in range(0, n):
                if isAdded[nbor]: continue

                costs[nbor] = min(costs[nbor], \
                    abs(points[toAdd][0] - points[nbor][0]) + abs(points[toAdd][1] - points[nbor][1]))
        
        return sumCost
