class Solution {
public:
    int myAtoi(string s) {
        
        if (s.empty()) return 0;

        int i = 0;

        // Automatically check we don't go out of bounds
        while (s[i] == ' ') i++;
        
        int sign = 1;
        
        if (s[i] == '-' || s[i] == '+') {
            if (s[i] == '-') sign = -1;
            i++;
        }
        
        int num = 0;
       
        while (s[i] >= '0' && s[i] <= '9') {
            // 7 because INT_MAX % 10 == 7
            // str(-2**31) satisfies .. s[c] > '7' and return -2**31
            if ((num > INT_MAX / 10) || 
               (num == INT_MAX / 10 && s[i] - '0' > 7)) {
                return sign == 1 ? INT_MAX : INT_MIN;
            }
 
            num = num * 10 + (s[i] - '0');
            i++;
       }   
       return sign * num;
    }
};