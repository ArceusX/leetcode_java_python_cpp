import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max_length = 0;
        int start = 0;
        HashMap<Character, Integer> chars = new HashMap<>();

        /*Algo: For each char, calculate longest substring that can be
                constructed from it and all other chars preceeding it, 
                excluding previous copy of same char, if one exists, 
                and chars preceding that previous copy. Compare these
                longest conditional substrings to get true longest.
        */
        
        /*Compare flow of strings "abcdba" vs "abcdbd"
            For abcdba, when 2nd b is encountered, var start is set to index of
            c, char proceeding b, which is encountered a 2nd time in
            current scanned substring. Thus, for 2nd b, longest substring
            that can be constructed with that 2nd b excludes precious b copy 
            and chars preceeding the preceding b.

            Continuing onto 2nd a, start already set to index of c,
            start = Math.max(start, chars.get(c) + 1) excludes all those
            already excluded chars, even if some of them follows first a.

            For char immediately following 2nd b: a vs d
            abcdba: start > chars.get(c) + 1. Chars considered: ab[cd]ba
            abcdbd: start < chars.get(c) + 1. Chars considered abcd[bd]
        */
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (chars.containsKey(c)) {
                start = Math.max(start, chars.get(c) + 1);
            }
            
            max_length = Math.max(max_length, i - start + 1);

            //Update previous copy of char for next potential copy of char
            chars.put(c, i);
        }
        
        return max_length;
        
    }
}