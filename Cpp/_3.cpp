#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max_length = 0;
        int start = 0;
        unordered_map<char, int> chars;
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.at(i);

            auto prev = chars.find(c);
            if (prev != chars.end()) {
                start = std::max(start, prev->second + 1);
            }
            
            max_length = max(max_length, i - start + 1);

            chars[c] = i;
        }
        
        return max_length;
    }
};