#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> chars;
        int max_length = 0;
        int start = 0;
        
        for (int end = 0; end < s.length(); end++) {
            char c = s.[end];

            auto prev = chars.find(c);
            if (prev != chars.end()) {
                start = std::max(prev->second + 1, start);
            }
            
            max_length = max(max_length, end - start + 1);

            chars[c] = end;
        }
        
        return max_length;
    }
};