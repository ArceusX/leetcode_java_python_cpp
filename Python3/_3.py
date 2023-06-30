# 003: Longest Substring Without Repeating Characters

# Target substr must not repeat any char c. For each c,
# if c is in prevSeen, exclude c and any char preceding
# c (ie lowBound = max(lowBound, prevSeen[c] + 1))
# Compare len(target) to running maxSublen

# a, b, c, d*, c , b  -> Check [abcd]. lowBound == a
# a, b, c, d , c*, b  -> Check [dc  ]. lowBound == d
# a, b, c, d , c , b* -> Check [dcb ]. lowBound == d

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prevSeen  = {}
        maxSublen = 0
        lowBound  = 0
            
        for i, c in enumerate(s):
            if c in prevSeen:
                lowBound = max(lowBound, prevSeen[c] + 1)

            prevSeen[c] = i
            maxSublen = max(maxSublen, i - lowBound + 1)
            
        return maxSublen
        