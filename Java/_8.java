// 008: Convert string to int
// Skip leading whitespace; read -|+ if present; loop until char
// not convertible to digit: if appending digit would put result 
// out of bound, return bound, else append. Prepend - if found

class Solution {
    public int myAtoi(String s) {
        int sLen = s.length(), i = 0;
        while (i < sLen && Character.isWhitespace(s.charAt(i))) i++;

        boolean isNegative = false;
        if (i < sLen && (s.charAt(i) == '-' || s.charAt(i) == '+')) {
            isNegative = (s.charAt(i) == '-');
            i++;
        }

        int ret = 0;
        for (; i < sLen; i++) {
            if (!Character.isDigit(s.charAt(i))) break;

            int digit = s.charAt(i) - '0';

            // 7 because MAX_VALUE % 10 == 7. Either by this or by
            // normal end return, str(MIN_VALUE) returns MIN_VALUE
            if (ret  > Integer.MAX_VALUE/10 ||
               (ret == Integer.MAX_VALUE/10 && digit > 7)) {
                return isNegative ? Integer.MIN_VALUE : Integer.MAX_VALUE;
            }

            ret = 10 * ret + digit;

        }

        return isNegative ? -ret : ret;
    }
}