# Prim's Algo
# Prim's builds from 1 central component that adds lightest
# remaining edge (calculated as weight from node already
# added to one not added) each iter

# Prim 1: Using heapq to efficiently retrieve lightest edge
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        isAdded = [False] * n
        
        sumCost = 0
        nInMST = 0

        # Store (weight, node) being pointed to/newly added
        heap = [(0, 0)]
        
        while nInMST < n:
            weight, toNode = heapq.heappop(heap)
            
            # Only add nodes not already added. If added, skip
            if isAdded[toNode]:
                continue
            
            isAdded[toNode] = True
            nInMST += 1
            sumCost += weight
            
            for nbor in range(n):

            	# Consider only edges carrying node not already added
                if not isAdded[nbor]:
                    addCost = abs(points[toNode][0] - points[nbor][0]) +\
                                  abs(points[toNode][1] - points[nbor][1])
                    
                    heapq.heappush(heap, (addCost, nbor))
                    
        return sumCost

# For Prim 1, heap calculates lowest cost edge. Main func checks if node
# it points to is not already added [after] edge is considered. Thus,
# every edge is stored, then from min edge, record min cost to node

# For Prim 2, main func itself retrieves lowest-cost node and checks if it
# is not added [awhile] edge is retrieved. Array stores min cost for each
# node rather than cost of each edge, which may not be lowest for node
# Thus, weight of node that depends on min edge is obtained directly

# Prim 2
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        sumCost = 0
        
        isAdded = [False] * n
        
        minCost = [float('inf')] * n
        minCost[0] = 0

        for nInMST in range(0, n):
            # Add node not added with lowest addCost, mark it added, then..
            toAdd = -1
            currMinCost = float('inf')
            for prospect in range(n):
                if not isAdded[prospect] and minCost[prospect] < currMinCost:
                    currMinCost = minCost[prospect]
                    toAdd = prospect
            
            sumCost += currMinCost
            isAdded[toAdd] = True
            
            # .. if weight from added node to any nbor not already added
            # is less than nbor's current cost. If so, update nbor's cost
            for nbor in range(n):
                if not isAdded[nbor]:
                    minCost[nbor] = min(minCost[nbor], abs(points[toAdd][0] - points[nbor][0]) +\
                         abs(points[toAdd][1] - points[nbor][1]))
        
        return sumCost
