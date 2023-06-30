// 007: Reverse Integer
// If reversed would go out of [-2^31, 2^31 - 1] range, return 0 instead

class Solution {
public:
    int reverse(int x) {

        int ret = 0;
        while (x != 0) {
            int leastSign = x % 10;
            x /= 10;

            // (2^31 - 1) % 10 == 7
            if ((ret > INT_MAX/10) || (ret == INT_MAX/10 && leastSign >  7)) return 0;
            if ((ret < INT_MIN/10) || (ret == INT_MIN/10 && leastSign < -8)) return 0;

            ret = 10 * ret + leastSign;
        }
        return ret;
    }
};