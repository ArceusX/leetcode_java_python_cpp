class Solution {
public:
    string multiply(string n1, string n2) {
        if (n1 == "0" || n2 == "0") return "0";
        
        int n1Len = n1.length();
        int n2Len = n2.length();
        int prodLen = n1Len + n2Len;

        //99 * 99 = 9801
        //Initialize all values to 0
        int* product = new int [n1Len + n2Len]();

        //Iterate right to left: i1 spaces left of rightmost
        for (int i1 = 0; i1 < n1Len; i1++) {

            //r == i1 + i2, but for this loop, initially i1 is 0
            for (int i2 = 0, r = i1; i2 < n2Len; i2++, r++) {
                product[r] += (n1[n1Len - i1 - 1] - '0') * 
                              (n2[n2Len - i2 - 1] - '0');

                if (product[r] > 9) { 
                    product[r + 1] += product[r] / 10;
                    product[r] = product[r] % 10;
                }
            }
        }

        string str;
        for (int i1 = 0; i1 < prodLen; i1++) {
            // Read from right to left of product array. (Leading) zeroes 
            // with no non-zero to their right are ignored. 009 -> 9
            if (str.length() == 0 && product[prodLen - 1 - i1] == 0) {
                continue;
            }
            str.push_back(product[prodLen - 1 - i1] + '0');
        }
        return str;
    }
};