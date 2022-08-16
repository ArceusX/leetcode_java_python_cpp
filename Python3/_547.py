# Disjoint union set: Return # of connected components
# See _547.java for algo

class Solution:
    def findCircleNum(self, conn: List[List[int]]) -> int:
        n = len(conn)
        
        parent = [x for x in range(n)]
        
        def find(x: int) -> int:
            while parent[x] != x:

         		# Wire x to point to its grandparent, which may
         		# be identical to parent. Then move x up group
                x, parent[x] = parent[x], parent[parent[x]]
            
            return x
        
        for row in range(0, n):
            for col in range(0, row):
                
                if conn[row][col] == 1:
                    parent[find(col)] = row;

                    #Path compression: probably unnecessary
                    #parent[col] = row
                    
        nGroups = 0
        for row in range(0, n):
            if parent[row] == row:
                nGroups += 1
                
        return nGroups