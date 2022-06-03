class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif len(needle) > len(haystack):
            return -1

        j = 0
        start = 0
        current = 0
        while (j < len(needle) and current < len(haystack)):

            #If find match, increment char in both strings
            if needle[j] == haystack[current]:
                current += 1
                j += 1

            # Reset found portion of needle and eliminate
            # current "start" because it has been checked
            else:
                j = 0
                start += 1
                current = start

        #If found, get start index by subtracting len of needle from end index
        if j == len(needle):
            return (current - j)
        else:
            return -1

'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0
        elif len(needle) > len(haystack):
            return -1

        needleLeng = len(needle)

        # After (len(haystack) - needleLength) char, what remains of haystack
        # has smaller len than needleLen
        for i in range(len(haystack) - needleLen + 1):
            #Slide window. Use list comprehension
            if haystack[i:i + needleLen] == needle:
                return i
        return -1
'''
