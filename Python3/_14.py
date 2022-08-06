class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestStr = min(strs, key=len)

        prefix = []
        for i, char in enumerate(shortestStr):
        	for string in strs:
        		if (char != string[i]): return "".join(prefix)

        	prefix.append(char)

        return "".join(prefix)