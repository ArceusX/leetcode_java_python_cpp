class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        isValid = [False for _ in range(len(s) + 1)]

        # Set each substring able to be splitted into itself
        # s[0:0] assumed to be valid substring of wordDict
        isValid[0] = True
        
        maxLen = max(len(w) for w in wordDict)
        
        for i in range(1, len(s) + 1):
            j = i - 1

            # End checking for current i if maxLen word is
            # shorter than s[j:i] (if maxLen + j < i)
            while (j >= 0 and (j + maxLen) >= i):

                # Check when splitting s[0:i] into s[0:j] and s[j:i],
                # whether s[0:j] can already be splitted and 
                # newly check if s[j:i] is a word within wordDict
                isValid[i] = isValid[j] and (s[j:i] in wordDict)
                
                if isValid[i]:
                    break
                    
                j -= 1
                
        return isValid[-1]
        
        