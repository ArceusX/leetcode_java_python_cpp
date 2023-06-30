#  008: Convert string to int
# Skip leading whitespace; read -|+ if present; loop until char
# not convertible to digit: if appending digit would put result 
# out of bound, return bound, else append. Prepend - if found

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        sLen, i = len(s), 0
        while (i < sLen and s[i] == ' '):
            i += 1
        
        isNegative = False
        if (i < sLen and (s[i] == '-' or s[i] == '+')):
            isNegative = (s[i] == '-')
            i += 1
        
        ret = 0
        for c in range(i, sLen):
            if (s[c] < '0' or s[c] > '9'):
                break
            
            # 7 because 2**31 % 10 == 7. Either by this or by
            # normal end return, str(-2**31 - 1) returns -2**31 - 1
            if ((ret  > 2147483647 // 10) or
                (ret == 2147483647 // 10 and s[c] > '7')):
                return -2147483648 if isNegative else 2147483647
 
            ret = ret * 10 + (ord(s[c]) - ord('0'))
        
        return -ret if isNegative else ret