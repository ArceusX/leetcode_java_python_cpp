// 007: Reverse Integer
// If reversed would go out of [-2^31, 2^31 - 1] range, return 0 instead
 
class Solution {
public int reverseerse(int x) {
    int ret = 0;
    while (x != 0) {
        int leastSig = x % 10;
        x /= 10;
        
        // (2^31 - 1) % 10 == 7
        if (ret > Integer.MAX_VALUE/10 || (ret == Integer.MAX_VALUE / 10 && leastSig >  7)) return 0;
        if (ret < Integer.MIN_VALUE/10 || (ret == Integer.MIN_VALUE / 10 && leastSig < -8)) return 0;
        ret = ret * 10 + leastSig;
    }
    return ret;
}
}