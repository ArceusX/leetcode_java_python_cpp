class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        
        parent = [x for x in range(len(mat) + 1)]
        
        def find(x: int) -> int:
            while parent[x] != x:

         		#Wire x to point to its grandparent, which may
         		#be identical to parent. Then move x up group
                x, parent[x] = parent[x], parent[parent[x]]
            
            return x
        
        for row in range(0, len(mat)):
            for col in range(0, row):
                
                if mat[row][col] == 1:
                    parent[find(col)] = row;

                    #Path compression: probably unnecessary
                    #parent[col] = row
                    
        nGroups = 0
        for row in range(0, len(mat)):
            if parent[row] == row:
                nGroups += 1
                
        return nGroups