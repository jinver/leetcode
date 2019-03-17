# You are given coins of different denominations and a total amount of money amount. Write a function 
# to compute the fewest number of coins that you need to make up that amount. If that amount of money 
# cannot be made up by any combination of the coins, return -1.

# Notes
# min num of coins for x=30, is the min of all possible combos of x-coins
# x - 25
# x - 10
# x - 5
# x - 1

import sys

class Solution:
    def coinChange(self, coins, amount) -> int:
        cache = {}
        coins.sort(reverse=True)
        return self.change(coins, amount, cache)

    def change(self, coins, amount, cache):
        if amount in cache: return cache[amount]
        if amount in coins:
            return 1
        elif amount == 0: 
            return 0
        print('calling change: ', amount)
        minimum = sys.maxsize
        for coin in coins:
            remainder = amount - coin
            if remainder >= 0:
                c = self.change(coins, remainder, cache)
                if c != -1 and c+1 < minimum:
                    minimum = c+1
        if minimum == sys.maxsize:
            minimum = -1
        cache[amount] = minimum
        return minimum
