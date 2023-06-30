class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        shortestStr = min(strs, key=len)

        for i, c in enumerate(shortestStr):
            for s in strs:
                if c != s[i]:
                    return shortestStr[:i]

        return shortestStr