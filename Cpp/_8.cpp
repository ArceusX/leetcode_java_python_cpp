class Solution {
public:
    int myAtoi(string s) {
        
        if (s.empty()) {
            return 0;
        }
        int i = 0;
        
        while (s[i] == ' ') {
            i++;
        }
        
        int sign = 1;
        
        if (s[i] == '-' || s[i] == '+'){
            sign = s[i] == '+' ? 1 : -1;
            i++;
        }
        
        if (s[i] - '0' < 0 || s[i] - '0' > 9) {
            return 0;
        }
        
        int num = 0;
       
        while (s[i] >= '0' && s[i] <= '9') {
            /*For INT_MAX == 64, if current char digit > 6, next
              char digit will push num to be greater than INT_MAX.
              Also, if current digit is 6 and next digit > 4.
              7 because 2^31 % 10 == 8
            */
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