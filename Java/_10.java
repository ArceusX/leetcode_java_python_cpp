class Solution {
    public boolean isMatch(String s, String p) {

        int sizeS = s.length();
        int sizeP = p.length();

        boolean[][] arr = new boolean[sizeS + 1][sizeP + 1];

        arr[0][0] = true;
        for (int i = 2; i < sizeP + 1; i++) {
            if (p.charAt(i - 1) == '*') {
                arr[0][i] = arr[0][i - 2];
            }
        }
        
        for (int i = 1; i < sizeS + 1; i++) {
            for (int j = 1; j < sizeP + 1; j++) {
                if (s.charAt(i - 1) == p.charAt(j - 1) || p.charAt(j - 1) == '.') {
                    arr[i][j] = arr[i - 1][j - 1];
                } else if (j > 1 && p.charAt(j - 1) == '*') {
                    arr[i][j] = arr[i][j - 2];
                    if (p.charAt(j - 2) == '.' || p.charAt(j - 2) == s.charAt(i - 1)) {
                        arr[i][j] = arr[i][j] | arr[i - 1][j];
                    }
                }
            }
        }
        return arr[sizeS][sizeP];
    }
}