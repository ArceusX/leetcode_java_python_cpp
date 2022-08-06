"""
For previously unseen char, store its index in dict,
    calculate length from "start" to it, and get higher
    between that length and maxLen. If recounter char,
    move start to index after previous index of duplicate
    [if] that previous index follows current start.
    Exclude from sequence last previous copy of duplicate
    char and any char preceding that previous copy.
    For each char, eval longest sequence containing it

[a+b+c+d+e]         -> Eval [abcd(e)]
[a+b+c+d+e] + c     -> Eval [de(c)]
[a+b+c+d+e] + c + b -> Eval [dec(b)]
"""

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        maxLen = 0
        start = 0
            
        for end, c in enumerate(s):
            if c in chars:
                start = max(chars[c] + 1, start)

            chars[c] = end
            maxLen = max(maxLen, end - start + 1)
            
        return maxLen
        