class Solution {
    public String minWindow(String t, String p) {
        int iTStart = 0, iTEnd = 0, minIT = 0;
        int nToFind = p.length(), minLen = Integer.MAX_VALUE;
        
        
        Map<Character, Integer> toFind = new HashMap<>();
        
        for (char ch : p.toCharArray()) {
            toFind.put(ch, toFind.getOrDefault(ch, 0) + 1);
        }
        
        while (iTEnd < t.length()) {
            
            if (toFind.containsKey(t.charAt(iTEnd))) {
                if (toFind.get(t.charAt(iTEnd)) > 0) nToFind--;
                toFind.put(t.charAt(iTEnd), toFind.get(t.charAt(iTEnd)) - 1);
            }
            
            iTEnd++;
            
            while (nToFind == 0) {
                
                if (iTEnd - iTStart < minLen) {
                    minLen = iTEnd - iTStart;
                    minIT = iTStart;
                }
                
                if (toFind.containsKey(t.charAt(iTStart))) {
                    if (toFind.get(t.charAt(iTStart)) == 0) {
                      nToFind++;  
                    }
                    toFind.put(t.charAt(iTStart), toFind.get(t.charAt(iTStart)) + 1);
                }
                
                iTStart++;
            }
        }
        
        return minLen != Integer.MAX_VALUE ? t.substring(minIT, minIT + minLen) : "";
    }
}