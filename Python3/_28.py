class Solution:
    def strStr(self, hay: str, needle: str) -> int:
        if not needle:
            return 0
        elif len(hay) < len(needle):
            return -1

        # Keep 2 points (start, end) for hay and 1 for needle
        iNEnd = 0
        iHStart = 0
        iHEnd = 0
        while (iNEnd < len(needle) and iHEnd < len(hay)):

            # If find match, ++ current ends in both strings
            if needle[iNEnd] == hay[iHEnd]:
                iHEnd += 1
                iNEnd += 1

            # Reset needle to none found and ++ iHstart because
            # we just checked starting from that in hay
            else:
                iNEnd = 0
                iHStart += 1
                iHEnd = iHStart

        # Finished checking needle (success) or hay (failure)
        if iNEnd == len(needle):
            return iHStart;
        else:
            return -1

'''
# List comprehension makes sliding window easier and quicker
class Solution:
    def strStr(self, hay: str, needle: str) -> int:

        if not needle:
            return 0
        elif len(needle) > len(hay):
            return -1

        needleLen = len(needle)

        # Consider only chars in hay that if is start, matching
        # end dependent on needleLen remains within hay
        for i in range(len(hay) - needleLen + 1):
            # Slide window of length needleLen in hay
            if hay[i:i + needleLen] == needle:
                return i

        return -1
'''
