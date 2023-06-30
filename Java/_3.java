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
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> prevSeen = new HashMap<>();

        // maxStart: extraneous for this problem, but need
        // for related problem to return longest substr
        int lowBound = 0, maxSublen = 0, maxStart = 0;

        for (int i = 0, sLen = s.length(); i < sLen; i++) {

            Integer prev = prevSeen.get(s.charAt(i));
            if (prev != null) {
                lowBound = Math.max(lowBound, prev + 1);
            }
            
            int len = i - lowBound + 1;
            if (len > maxSublen) {
                maxSublen = len;

                // Extraneous for this specific problem
                if (prev != null) maxStart = prev + 1;
            }
            prevSeen.put(s.charAt(i), i);
        }

        return maxSublen;
    }
}