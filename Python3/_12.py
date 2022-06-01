# Prefix is a substr such that if char is included,
# any char preceding it must also be included

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lcp = ""
        
        if strs is None or len(strs) == 0:
            return lcp
            
        minLength = min(len(str) for str in strs)  
        

        # Length f lcp restricted to length of shortest str
        # Iterate through chars of any str, then check if
        # any char is missing in all other strs
        for i in range(0, minLength):
            current = strs[0][i]
            
            for j in range(0, len(strs)):
                if strs[j][i] != current:
                    return lcp
                
            lcp += current
            
        return lcp