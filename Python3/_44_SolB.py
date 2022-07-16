#SolB is Python implementation of _44.cpp

class Solution:
    def isMatch(self, t: str, p: str) -> bool:
        
        lenT, lenP = (len(t), len(p))
        iT = 0; iP = 0
        indexT = -1; indexP = -1
        
        while iT < lenT:
            if iP < lenP:
                if (p[iP] == t[iT]) or p[iP] == '?':
                    iT += 1
                    iP += 1
                    continue
                
                if p[iP] == '*':
                    iP += 1
                    indexP = iP
                    indexT = iT
                    continue
                
            if indexP > -1:
                iP = indexP
                indexT += 1
                iT = indexT
                
            else:
                return False
            
        while iP < lenP and p[iP] == "*":
            iP += 1
            
        return iP == lenP
                
                