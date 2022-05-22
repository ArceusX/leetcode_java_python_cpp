class Solution:
    def myAtoi(self, s: str) -> int:
        
        if not s:
            return 0
        
        i = 0
        
        while (i < len(s)):
            if (s[i] == ' '):
                i += 1
            else:
                break
        
        sign = 1
        
        if (i < len(s) and (s[i] == '-' or s[i] == '+')):
            sign = 1 if s[i] == '+' else -1
            i += 1
        
        if (i < len(s) and (s[i] < '0' or s[i] > '9')):
            return 0
        
        num = 0;
        
        INT_MAX = 2147483647
        INT_MIN = -2147483648
       
        for c in range(i, len(s)):
            if (s[c] < '0' or s[c] > '9'):
                break
            
            if ((num > INT_MAX // 10) or
               (num == INT_MAX // 10 and s[c] > '7')):
                return INT_MAX if sign == 1 else INT_MIN
 
            num = num * 10 + (ord(s[c]) - ord('0'))
        
        return sign * num
        