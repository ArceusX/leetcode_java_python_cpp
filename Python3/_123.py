# 188: Max Profit on 2 Pairs of Buys and Sells

# Dynamic programming: O(n) time
# Maximize sell profit up to today by solving 
# subproblem to minimize buy price up to yesterday
# Minimize buy  = price - max of prior sell
# Maximize sell = price - min of prior buy
# Initialize sell = 0; buy = upper bound of price
# for each before loop

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy1 , buy2  = 100001, 100001
        sell1, sell2 = 0, 0

        for price in prices:
            buy1  = min(buy1 , price)
            sell1 = max(sell1, price - buy1)
            buy2  = min(buy2 , price - sell1)
            sell2 = max(sell2, price - buy2 )

        return sell2
    