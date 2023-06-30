// Hard: Unmastered. Uses dynamic programming

class Solution {
    public boolean isMatch(String t, String p) {

        int sizeT = t.length();
        int sizeP = p.length();

        boolean[][] arr = new boolean[sizeP + 1][sizeT + 1];

        arr[0][0] = true;
        for (int j = 2; j < sizeP + 1; j++) {
            if (p.charAt(j - 1) == '*') {
                arr[j][0] = arr[j - 2][0];
            }
        }

        for (int j = 1; j < sizeP + 1; j++)
            for (int i = 1; i < sizeT + 1; i++) { {
                if (t.charAt(i - 1) == p.charAt(j - 1) || p.charAt(j - 1) == '.') {
                    arr[j][i] = arr[j - 1][i - 1];
                } else if (p.charAt(j - 1) == '*') {
                    arr[j][i] = arr[j - 2][i];
                    if (p.charAt(j - 2) == '.' || p.charAt(j - 2) == t.charAt(i - 1)) {
                        arr[j][i]  = arr[j][i] || arr[j][i - 1];
                    }
                }
            }
        }
        return arr[sizeP][sizeT];
    }
}