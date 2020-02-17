# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the 
# stock), design an algorithm to find the maximum profit.


class Solution:
    def maxProfit(self, prices) -> int:
        if not prices: return 0
        low = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            profit = prices[i] - low
            max_profit = max(profit, max_profit)
            low = min(prices[i], low)
        return max_profit