// 008: Convert string to int
// Skip leading whitespace; read -|+ if present; loop until char
// not convertible to digit: if appending digit would put result 
// out of bound, return bound, else append. Prepend - if found

class Solution {
public:
    int myAtoi(string s) {

        int i = 0;
        while (isspace(s[i])) i++;

        bool isNegative = false;
        if (s[i] == '-' || s[i] == '+') {
            isNegative = (s[i] == '-');
            i++;
        }

        int ret = 0;
        for (int sLen = s.size(); i < sLen; i++) {
            char c = s[i];
            if (!isdigit(c)) break;

            int digit = c - '0';

            // 7 because INT_MAX % 10 == 7. Either by this or by
            // normal end return , str(INT_MIN) returns INT_MIN
            if  (ret  > INT_MAX/10 || 
                (ret == INT_MAX/10 && digit > 7)) {
                return isNegative ? INT_MIN : INT_MAX;
            }

            ret = 10 * ret + digit;
        }

        return isNegative ? -ret : ret;
    }
};