# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# strategy: brute-force. have one loop check left side, another loop check right side. sliding window technique.
# second strategy: split array in half, compare min on left, max on right, and subtract. if negative then output = 0, if positive then output = max profit
#                  binary search style. But, its not a sorted array so it can be very complex to do such strategy.
# third strategy: one pass, add, stop, and check strategy. similar to twosum.py 

# third strat approach
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0

        for i in range (0, len(prices)):
            if(prices[i] < minPrice):
                minPrice = prices[i]

            if(prices[i] - minPrice > maxProfit):
                maxProfit = prices[i] - minPrice

        return maxProfit

