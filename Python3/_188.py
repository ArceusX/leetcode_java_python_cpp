# 188: Max Profit on k Pairs of Buys and Sells (see _123.py)

# Dynamic programming: O(nk) time; k is const
# Maximize sell profit up to today by solving 
# subproblem to minimize buy price up to yesterday
# Minimize buy  = price - max of prior sell
# Maximize sell = price - min of prior buy

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        buys  = (k + 1) * [1001]
        sells = (k + 1) * [0]

        for price in prices:
            for i in range(1, k + 1):
                buys [i] = min(buys [i], price - sells[i - 1])
                sells[i] = max(sells[i], price - buys [i    ])

        return sells[-1] # Profit of final (kth) sell
