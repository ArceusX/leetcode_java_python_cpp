// Greedy algo: Track sum. Every time we arrive at
// equal # of 'L's and 'R's, ++numBalanced

class Solution {
public:
int balancedStringSplit(string s) {
    int sum = 0, numBalanced = 0;
    for (const auto& c : s) {
        sum += (c == 'L' ? 1 : -1);
        if (sum == 0) ++numBalanced;
    }
    return numBalanced;        
}
};