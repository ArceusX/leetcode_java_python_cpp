# Kruskal's Algo, using disjoint union set to check if potential
# edge connects components not already connected.

# Unlike Prim's, Kruskal's does not build out from 1 central
# connected component, but rather from multiple (each node
# node initial placed in its own component) that are then
# finally merged into 1 central component
# ie No global "root", only local ones, until final iteration

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        parent = [x for x in range(n)]
        
        # Return root and height of path to root
        # Not global rank, but rather local based on 1 path
        def find(x: int) -> (int, int):
            height = 1
            while parent[x] != x:

         		# Wire x to point to its grandparent, which may
         		# be identical to parent. Then move x up branch
                x, parent[x] = parent[x], parent[parent[x]]
                height += 1
            
            return (x, height)
        
        edges = []
        
        # Calculate Manhattan distance from every node to every other
        for outNode in range(n):
            for inNode in range(outNode + 1, n):
                weight = abs(points[outNode][0] - points[inNode][0]) +\
                         abs(points[outNode][1] - points[inNode][1])
                edges.append((weight, outNode, inNode))
                
        edges.sort()
        
        # For minimun spanning tree, V = E + 1
        nInMST = 0
        sumCost = 0
        
        for (weight, outNode, inNode) in edges:
            outFind = find(outNode)
            inFind = find(inNode)

            if (outFind[0] != inFind[0]):
                sumCost += weight
                nInMST += 1
                
                if nInMST == n - 1:
                    break
                
                # Wire root of shorter height to root of longer
                # (using rank or longest height over any path would 
                # be improved, costlier alternative)
                if (outFind[1] > inFind[1]):
                    parent[inFind[0]] = outFind[0]
                else:
                    parent[outFind[0]] = inFind[0]
                    
        return sumCost
    