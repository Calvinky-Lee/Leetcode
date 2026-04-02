# Last updated: 4/2/2026, 1:44:46 PM
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = max(nums)
        for i in nums:
            if abs(i) < abs(closest):
                closest = i
            elif abs(i) == abs(closest):
                closest = max(i, closest)
        return closest

        