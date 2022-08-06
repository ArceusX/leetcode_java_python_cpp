class Solution {
    public String multiply(String n1, String n2) {

        if (n1.equals("0") || n2.equals("0")) return "0";

        int n1Len = n1.length();
        int n2Len = n2.length();

        //99 * 99 = 9801
        int[] product = new int[n1Len + n2Len];

        //Iterate right to left
        for (int i1 = n1Len - 1; i1 >= 0; i1--) {

            // r is initially n2Len + n1Len - 1, for i1 = n1Len - 1
            // r-- when either i1-- or i2--. Thus r = n2Len + i1
            for (int i2 = n2Len - 1, r = n2Len + i1; i2 >= 0; i2--, r--) {
                product[r] += (n1.charAt(i1) - '0') * 
                              (n2.charAt(i2) - '0');

                if (product[r] > 9) { 
                    product[r - 1] += product[r] / 10;
                    product[r] = product[r] % 10;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < product.length; i++) {
            // Write product [] to sb left to right
            // Ignore (leading) zeroes with no non-zero to their left
            // 009 -> 9. Simply checking char to left suffices
            if (sb.length() == 0 && product[i] == 0) {
                continue;
            }
            sb.append(product[i]);
        }
        return sb.toString();
    }
}