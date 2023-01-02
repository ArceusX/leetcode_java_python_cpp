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
        
        // Set each substring able to be splitted into itself
        // s[0:0] assumed to be valid substring of wordDict
        isValid[0] = true;

        int maxLen = getMaxLength(wordDict);

        for (int i = 1; i <= s.length(); i++) {
            
            // End checking for current i if maxLen word is
            // shorter than s[j:i] (if maxLen + j < i)
            for (int j = i - 1; j >= 0 && i <= maxLen + j; j--) {
                
                // Check when splitting s[0:i] into s[0:j] and s[j:i],
                // whether s[0:j] can already be splitted and 
                // newly check if s[j:i] is a word within wordDict
                isValid[i] = isValid[j] && wordDict.contains(s.substring(j, i));

                if (isValid[i]) {
                    break;
                }
            }
        }
        
        // Return whether entire string can be splitted
        return isValid[s.length()];
    }
}