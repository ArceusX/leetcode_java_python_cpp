class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        i = 0
        while (i < len(s) and s[i] == ' '):
            i += 1
        
        sign = 1
        if (i < len(s) and (s[i] == '-' or s[i] == '+')):
            if s[i] == '-':
                sign = -1

            i += 1
        
        num = 0;
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
       
        for c in range(i, len(s)):
            if (s[c] < '0' or s[c] > '9'):
                break
            
            # 7 because INT_MAX % 10 == 7
            # str(-2**31) satisfies .. s[c] > '7' and return -2**31
            if ((num > INT_MAX // 10) or
               (num == INT_MAX // 10 and s[c] > '7')):
                return INT_MAX if sign == 1 else INT_MIN
 
            num = num * 10 + (ord(s[c]) - ord('0'))
        
        return sign * num