/* Dynamic Programming: 
   str is "valid" if it is splittable into "valid" substr and word
   in wordDict. Anchoring i, sliding j given (j < i) to 0, if s[j:i]
   is in wordDict, str inherits validity of its substr str[0:j]
   If str[0:j] was earlier marked valid, str[0:i] will also be valid 
*/
   
class Solution {
    private int getMaxLength(List<String> wordDict) {
        int max = 0;
        for (String word: wordDict) {
            if (word.length() > max) {
                max = word.length();
            }
        }
        return max;
    }
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] isValid = new boolean[s.length() + 1];
        
        // To affirm s[0:i] is splittable into s[0:0] and s[0:i]
        // and if s[0:i] is in wordDict, s[0:i] should be marked
        // true and for that, isValid[0] needs to be already true
        isValid[0] = true;

        // Flag early-exit of iteration i if length of s[j:i] 
        // exceeds maxLen of any word in wordDict
        int maxLen = getMaxLength(wordDict);

        // i is window-end. This outer-loop shifts window-end right 
        for (int i = 1; i <= s.length(); i++) {
            
            // Stop slide once end reached or if length of s[j:i] 
            // exceeds maxLen of any word that exists in wordDict
            for (int j = i - 1; j >= 0 && maxLen >= i - j; j--) {
                
                // Check when splitting s[0:i] into s[0:j] and s[j:i],
                // whether s[0:j] can already be splitted and 
                // newly check if s[j:i] is a word within wordDict
                isValid[i] = isValid[j] && wordDict.contains(s.substring(j, i));

                // Need only 1 pair of s[0:j] and s[j:i]
                if (isValid[i]) break;
            }
        }
        
        // Return if entire str is splittable
        return isValid[s.length()];
    }
}