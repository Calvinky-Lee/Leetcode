# Last updated: 4/2/2026, 1:44:46 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini = 1
        maxi = max(piles)
        result  = maxi

        while mini <= maxi:
            hours = 0
            mid = mini + (maxi - mini)// 2

            for i in piles:
                hours += math.ceil(i/mid)
            
            if hours <= h:
                result = min(result, mid)
                maxi = mid - 1
            else:
                mini = mid + 1
        return result

