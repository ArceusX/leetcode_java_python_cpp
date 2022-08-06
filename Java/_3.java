/*
For previously unseen char, store its index in dict,
    calculate length from "start" to it, and get higher
    between that length and maxLen. If recounter char,
    move start to index after previous index of duplicate
    [if] that previous index follows current start.
    Exclude from sequence last previous copy of duplicate
    char and any char preceding that previous copy.
    For each char, eval longest sequence containing it

[a+b+c+d+e]         -> Eval [abcd(e)]
[a+b+c+d+e] + c     -> Eval [de(c)]
[a+b+c+d+e] + c + b -> Eval [dec(b)]
*/

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> chars = new HashMap<>();
        int maxLen = 0;
        int start = 0;

        for (int end = 0; end < s.length(); end++) {
            char c = s.charAt(end);

            Integer prev = chars.get(c);
            if (prev != null) {
                start = Math.max(prev + 1, start);
            }
            
            maxLen = Math.max(maxLen, end - start + 1);

            // Set last previous copy of char for potential next
            chars.put(c, end);
        }
        
        return maxLen;
    }
}