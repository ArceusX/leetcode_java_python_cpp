class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        
        int current = x;
        long reverse = 0;
        
        while (current != 0) {
            reverse = reverse * 10 + current % 10;
            current /= 10;
        }
        
        return (long)x == reverse;
    }
};