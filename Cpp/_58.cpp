class Solution {
public:
    int lengthOfLastWord(string s) {
        
        int i = s.length() - 1;
        for (; i >= 0; i-- ) {
            if (!isspace(s[i])) break;
        }
        
        int start = i;
        for (; i >= 0; i--) {
            if (isspace(s[i])) break;
        }
        return start - i;                               
    }
};