class Solution {
    public int strStr(String hay, String needle) {
    	if (needle.length() == 0) return 0;
    	else if (hay.length() < needle.length()) return -1;

    	int iNeedleEnd = 0;
    	int iHayStart = 0;
    	int iHayEnd = 0;

    	while (iNeedleEnd < needle.length() && iHayEnd < hay.length()) {
    		if (needle.charAt(iNeedleEnd) == hay.charAt(iHayEnd)) {
    			iNeedleEnd++;
    			iHayEnd++;
    		}
    		else {
    			iNeedleEnd = 0;
    			iHayStart++;
    			iHayEnd = iHayStart;
    		}
    	}

    	if (iNeedleEnd == needle.length()) return iHayStart;
    	else return -1;
    }
}