/* Rather than compare sorted s and sorted t, count freq of
   each char a-z for each and return True if counts all equal
*/

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        int counts [26] = {0};

        for (int i = 0, len = s.size(); i < len; i++) {
            counts[s[i] - 'a']++;
            counts[t[i] - 'a']--;
        }

        for (int i = 0; i < 26; i++) {
            if (counts[i] != 0) return false;
        }

        return true;
    }
};