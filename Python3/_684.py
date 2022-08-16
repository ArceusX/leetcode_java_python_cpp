"""
Algo: For minimum spanning tree, each edge added during
      its construction connects 2 nodes not already
      reachable via intermediates in same set. Edge that
      connects two already reachable nodes ruins MST.
      With disjoint union set, label reachable nodes as
      belong to same set; if another edge connects 2 nodes
      already in same set/reachable, new edge is excess.
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # Problem: Vertices given as 1 to n. Entry 0 is unused
        parent = [x for x in range(len(edges)+1)]

        def find(x):
            while parent[x] != x:
                x, parent[x] = parent[x], parent[parent[x]]
            return x
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY: return True
            
            parent[rootX] = rootY

        for x, y in edges:
            if union(x,y): return [x, y]