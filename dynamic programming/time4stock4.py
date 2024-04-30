#You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

#Find the maximum profit you can achieve. You may complete at most k transactions.

#Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

#Input: k = 2, prices = [2,4,1]
#Output: 2
#Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

# kadane's algo

from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if 2*k >= len(prices): 
            return sum(max(0, prices[i]-prices[i-1]) for i in range(1, len(prices)))
        
        pnl = [0]*len(prices)
        for _ in range(k):
            val = 0
            for i in range(1, len(pnl)): 
                val = max(pnl[i], val + prices[i] - prices[i-1]) 
                pnl[i] = max(pnl[i-1], val)
        return pnl[-1]