class Solution {
public:
    string multiply(string n1, string n2) {

        if (n1 == "0" || n2 == "0") return "0";
        
        int n1Len = n1.length(), n2Len = n2.length();
        int prodLen = n1Len + n2Len;

        // 99 * 99 = 9801:
        // Initialize all values to 0
        int* product = new int [n1Len + n2Len]();

        //Iterate right to left
        for (int i1 = n1Len - 1; i1 >= 0; i1--) {

            // r is initially n2Len + n1Len - 1, for i1 = n1Len - 1
            // r-- when either i1-- or i2--. Thus r = n2Len + i1
            for (int i2 = n2Len - 1, r = n2Len + i1; i2 >= 0; i2--, r--) {
                product[r] += (n1[i1] - '0') * 
                              (n2[i2] - '0');

                if (product[r] > 9) { 
                    product[r - 1] += product[r] / 10;
                    product[r] = product[r] % 10;
                }
            }
        }

        string str;
        int i = 0;
        for (; i < prodLen; i++) {
            // Write product [] to sb left to right
            // Ignore (leading) zeroes ie (009 -> 9)
            if (product[i] != 0) break;
        }

        for (; i < prodLen; i++) str.push_back(product[i] + '0');
        return str;
    }
};