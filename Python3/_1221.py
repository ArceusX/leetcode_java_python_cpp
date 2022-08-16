# Greedy algo: Track sum. Every time we arrive at
# equal # of 'L's and 'R's, ++numBalanced

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        numBalanced = 0
        sum_ = 0

        for char in s:
        	sum_ += 1 if char == 'L' else -1;
        	if sum_ == 0:
        		numBalanced += 1

        return numBalanced