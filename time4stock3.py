# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete at most two transactions.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# make an array that holds the two maxes. if value > maxValue[1] put in 1, if value < maxValue[1] && value > maxValue[0] put in 0

# solution below is partial and gives a close answer to expected. The tweek that needs to be made is having the algorithim do two transactions
# rather than multiple and accounting for the best two. Current algorithim is doing partial dp

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        maxValue = [0,0]

        for i in range(1, len(prices)):
            if(prices[i] > prices[i - 1]):
                maxProfit = prices[i] - prices[i - 1]
                if(maxProfit > maxValue[1]):
                    maxValue[1] = maxProfit
                elif(maxProfit < maxValue[1] and (maxProfit > maxValue[0])):
                    maxValue[0] = maxProfit

        maxProfit = maxValue[0] + maxValue[1]
        return maxProfit

# best solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstStockPrice = prices[0]
        firstProfit = 0

        secondStockPrice = -prices[0]
        secondProfit = 0

        for currPrice in prices:
            firstStockPrice = min(firstStockPrice, currPrice) # buys the cheapest stock
            firstProfit = max(firstProfit, currPrice - firstStockPrice) # sells it at the highest in the array

            secondStock = max(secondStockPrice, firstProfit - currPrice) # buys the cheapest stock
            secondProfit = max(secondProfit, secondStock + currPrice) # sells it at the highest in the array
        return secondProfit
