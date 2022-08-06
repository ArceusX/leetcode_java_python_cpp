class Solution {
    public int reverseerse(int x) {
        int reverse = 0;
        while (x != 0) {
            int leastSig = x % 10;
            if (reverse > Integer.MAX_VALUE/10 || (reverse == Integer.MAX_VALUE / 10 && leastSig > 7)) return 0;
            if (reverse < Integer.MIN_VALUE/10 || (reverse == Integer.MIN_VALUE / 10 && leastSig < -8)) return 0;
            reverse = reverse * 10 + leastSig;
            x /= 10;
        }
        return reverse;
    }
}