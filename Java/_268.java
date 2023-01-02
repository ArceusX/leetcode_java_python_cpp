/*
XOR is commutative (for sequence of only XOR
operations, order of operands doesn't matter). 
a XOR a == 0, 0 XOR a == a. If XOR each val in
[]nums, then XOR each int in range [1:n], inclusive,
two counts of each non-missing int cancels each other 
to make result 0, then 0 XOR missing int == missing int
*/

class Solution {
    public int missingNumber(int[] nums) {
        int prod = 0;

        int i = 1;
        for (int num : nums) {
        	prod ^= num;
        	prod ^= i;
            i++;
        }

        return prod;
    }
}