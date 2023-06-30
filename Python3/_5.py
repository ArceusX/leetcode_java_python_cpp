# 005: Longest Palindromic Substring

# Center char of palindrome doesn't need to have mirror
# Center can represent palindromic substr of 1 repeated
# char. Then check for mirrors from center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)
        if sLen < 2: return s

        # maxLeft: left for current maxSublen
        center, maxSublen, maxLeft = 0, 1, 0

        # While possibility of any sublen > maxSublen by
        # expanding in boths directions from center
        while center + maxSublen / 2 < sLen:
            left = right = center

            # Get right (end) of longest chain of repeated
            # char at left. This chain is palindromic
            while (right < sLen - 1) and s[left] == s[right + 1]:
                right += 1

            # Evaluating center for any in palindrome of 1 char
            # repeated means center evaluated for all repeats
            center = right + 1
            
            # Extend from palindrome of 1 char repeated:
            # compare chars on left and right edges 
            while (right < sLen - 1) and (left > 0) and s[right + 1] == s[left - 1]:
                left -= 1
                right += 1

            if  maxSublen < right - left + 1:
                maxSublen = right - left + 1
                maxLeft   = left

        return s[maxLeft:maxLeft + maxSublen]