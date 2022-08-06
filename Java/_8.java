class Solution {
    public int myAtoi(String s) {
        if (s.isEmpty()) return 0;

        int i = 0;
        while (i < s.length() && s.charAt(i) == ' ') i++;

        int sign = 1;
        if (i < s.length() && (s.charAt(i) == '-' || s.charAt(i) == '+')) {
            if (s.charAt(i) == '-') sign = -1;
            i++;
        }

        int num = 0;
        while (i < s.length()) {
            if (s.charAt(i) < '0' || s.charAt(i) > '9') break;

            if ((num > Integer.MAX_VALUE / 10) ||
                    (num == Integer.MAX_VALUE / 10 && s.charAt(i) > '7')) {
                return (sign == 1) ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }

            num = 10 * num + (s.charAt(i) - '0');
            i++;
        }

        return sign * num;
    }
}