class Solution {
public:

    //Sample: aaaab
    string longestPalindrome(string s) {
        if (s.size() < 2) {
            return s;
        }
        
        int len = s.size(), start = 0, max_len = 1, left, right;
        for (int center = 0; center + max_len / 2 < len;) {
            left = right = center;
            
            //Build rightward until encounter different char
            while ((right < len - 1) && s[right + 1] == s[right]) {
                ++right;
            }
            
            /*Previous while loop gave us longest palindromic substring
              with single repeated char. Now test longest possible
              containing different char. Set center to it, then try to
              build out from both directions.
            */

            center = right + 1;
            while (right < len - 1 && left > 0 && s[right + 1] == s[left - 1]) {
                ++right;
                --left;
            }
            if (max_len < right - left + 1) {
                start = left;
                max_len = right - left + 1;
            }
        }
        return s.substr(start,max_len);
    }
};