// 003: Longest Substring Without Repeating Characters
/*
 * Target substr must not repeat any char c. For each c,
 * if c is in prevSeen, exclude c and any char preceding
 * c (ie lowBound = max(lowBound, prevSeen[c] + 1)) 
 * Compare len(target) to running maxSublen

 * a, b, c, d*, c , b  -> Check [abcd]. lowBound == a
 * a, b, c, d , c*, b  -> Check [dc  ]. lowBound == d
 * a, b, c, d , c , b* -> Check [dcb ]. lowBound == d */

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> prevSeen;

        // maxStart: extraneous for this problem, but need
        // for related problem to return longest substr
        int maxSublen = 0, lowBound = 0, maxStart = 0;
        
        for (int i = 0, sLen = s.length(); i < sLen; i++) {
            char c = s[i];

            auto prev = prevSeen.find(c);
            if (prev != prevSeen.end()) {
                lowBound = max(lowBound, prev->second + 1);
            }

            int len = i - lowBound + 1;
            if (len > maxSublen) {
                maxSublen = len;

                // Extraneous for this specific problem
                if (prev != prevSeen.end()) {
                    maxStart = prev->second + 1;
                }
            }

            prevSeen[c] = i;
        }
        return maxSublen;
    }
};