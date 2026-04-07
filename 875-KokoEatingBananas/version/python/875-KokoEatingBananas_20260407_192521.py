# Last updated: 4/7/2026, 7:25:21 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        mini = 1
4        maxi = max(piles)
5        result  = maxi
6
7        while mini <= maxi:
8            hours = 0
9            mid = mini + (maxi - mini)// 2
10
11            for i in piles:
12                hours += math.ceil(i/mid)
13            
14            if hours <= h:
15                result = min(result, mid)
16                maxi = mid - 1
17            else:
18                mini = mid + 1
19        return result
20
21