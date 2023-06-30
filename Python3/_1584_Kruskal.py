# 1584 Min Cost to Connect All Points (Kruskal's Algo)

# Kruskal
# Join components not already joined via min-weight edge
# Prim adds nodes to single connected component directly
# Kruskal instead adds nodes by merging n components
# (each node initially put in its own) until 1 remains

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        # Disjoint union set 
        parent = [x for x in range(n)]
        # Re: root of set holding x and height of path to that root
        # Height lets identify larger set to join other set to
        def find(x: int) -> (int, int):
            height = 1
            while parent[x] != x: # If !points to itself, is !root
                # Point x to its GP to shorten path
                x, parent[x] = parent[x], parent[parent[x]]
                height += 1
            
            return (x, height)
        
        # Sort by distance from every node to every other
        edges = []
        for outNode in range(n):
            for inNode in range(outNode + 1, n):
                weight = abs(points[outNode][0] - points[inNode][0]) +\
                         abs(points[outNode][1] - points[inNode][1])
                edges.append((weight, outNode, inNode))
        edges.sort()
        
        # .. =  1: Self-edge initializes each set with 1 node 
        nInMST  = 1
        sumCost = 0
        
        for (weight, outNode, inNode) in edges:
            outFind = find(outNode)
            inFind  = find(inNode)

            if (outFind[0] != inFind[0]): # Join sets not joined
                sumCost += weight
                nInMST  += 1
                
                if nInMST == n: break
                
                # Root of shorter height to point to longer root
                # To use rank or longest height over any path 
                # would be improved, costlier alternative
                if (outFind[1] > inFind[1]):
                    parent[inFind[0]] = outFind[0]
                else:
                    parent[outFind[0]] = inFind[0]
                    
        return sumCost
    