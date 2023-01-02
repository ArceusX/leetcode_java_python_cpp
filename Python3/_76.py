
# See _76.cpp for explanation of algo
class Solution:

	# t is text/haystack; p is pattern/needle to find
    def minWindow(self, t: str, p: str):

        iTEnd, iTStart, minStart = 0, 0, 0 
        nToFind = len(p)
        minLen = float('inf')
    
        toFind = defaultdict(int)
        for c in p:
            toFind[c] += 1
            
        while (iTEnd < len(t)):
            
            if t[iTEnd] in toFind:
                if toFind[t[iTEnd]] > 0:
                    nToFind -= 1
                toFind[t[iTEnd]] -= 1
            
            iTEnd += 1
            
            while (nToFind == 0):
                
                if (iTEnd - iTStart < minLen):
                    minLen = iTEnd - iTStart
                    minStart = iTStart
                    
                if t[iTStart] in toFind:
                    if toFind[t[iTStart]] == 0:
                        nToFind += 1
                        
                    toFind[t[iTStart]] += 1
                    
                iTStart += 1
                
        
        if (minLen != float('inf')):
            return t [minStart : minStart + minLen]
        else:
            return ""
