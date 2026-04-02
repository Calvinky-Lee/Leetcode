# Last updated: 4/2/2026, 1:44:55 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minprice = float('inf')

        for i in prices:
            if i < minprice:
                minprice = i
            elif i - minprice > profit:
                profit = i - minprice
        return profit