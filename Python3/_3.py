"""
Algo:For each char, calculate longest substring that can be
    constructed from it and all other chars preceeding it, 
    excluding previous copy of same char, if one exists, 
    and other chars preceding that previous copy. Compare
    these individual longest substrings to get absolute longest.


Compare flow of strings "abcdba" vs "abcdbd"
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
    abcdbd: start < chars.get(c) + 1. Chars considered abcd[bd]"""

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        start = 0
        max_length = 0
            
        for index, c in enumerate(s):
            if c in chars:
                start = max(start, chars[c] + 1)
                
            max_length = max(max_length, index - start + 1)
            chars[c] = index
            
        return max_length
        