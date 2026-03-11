# Last updated: 3/11/2026, 4:40:16 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        profit = 0
4        minprice = float('inf')
5
6        for i in prices:
7            if i < minprice:
8                minprice = i
9            elif i - minprice > profit:
10                profit = i - minprice
11        return profit