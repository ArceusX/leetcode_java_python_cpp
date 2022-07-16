class Solution {
public:
    int lengthOfLastWord(string s) {
        
        // If end != npos (no non-space in s), return will be nonsense
        // If end == npos (no space in s), return will give result
        // assuming space "exists" before s, for still right result
        int end = s.find_last_not_of(" ");
        return end - s.substr(0, end).find_last_of(" ");
    }
};