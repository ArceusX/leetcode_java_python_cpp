class Solution {
    public String multiply(String n1, String n2) {

        if (n1.equals("0") || n2.equals("0")) return "0";

        int n1Len = n1.length();
        int n2Len = n2.length();

        //99 * 99 = 9801
        int[] product = new int[n1Len + n2Len];

        //Iterate right to left: i1 spaces left of rightmost
        for (int i1 = 0; i1 < n1Len; i1++) {

            //r == i1 + i2, but for this loop, initially i1 is 0
            for (int i2 = 0, r = i1; i2 < n2Len; i2++, r++) {
                product[r] += (n1.charAt(n1Len - i1 - 1) - '0') * 
                              (n2.charAt(n2Len - i2 - 1) - '0');

                if (product[r] > 9) { 
                    product[r + 1] += product[r] / 10;
                    product[r] = product[r] % 10;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i1 = 0; i1 < product.length; i1++) {
            // Read from right to left of product array. (Leading) zeroes 
            // with no non-zero to their right are ignored. 009 -> 9
            if (sb.length() == 0 && product[product.length - 1 - i1] == 0) {
                continue;
            }
            sb.append(product[product.length - 1 - i1]);
        }
        return sb.toString();
    }
}