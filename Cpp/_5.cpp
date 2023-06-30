class Solution {
public:
    string longestPalindrome(string s) {
        int sLen = s.size();
        if (sLen < 2) return s;
        
        // maxLeft: left for current maxSublen
        int maxSublen = 1, maxLeft = 0, left, right;

        // While possibility of any sublen > maxSublen by
        // expanding in both directions from center
        for (int center = 0; center + maxSublen / 2 < sLen;) {
            left = right = center;
            
            // Get right (end) of longest chain of repeated
            // char at left. This chain is palindromic
            while ((right < sLen - 1) && s[left] == s[right + 1]) {
                ++right;
            }

            // Evaluating center for any in palindrome of 1 char
            // repeated means center evaluated for all repeats
            center = right + 1;

            // Extend from palindrome of 1 char repeated:
            // compare chars on left and right edges 
            while (right < sLen - 1 && left > 0 && s[right + 1] == s[left - 1]) {
                ++right;
                --left;
            }

            if (maxSublen < right - left + 1) {
                maxSublen = right - left + 1;
                maxLeft = left;
            }
        }
        return s.substr(maxLeft, maxSublen);
    }
};