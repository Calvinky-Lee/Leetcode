# Last updated: 3/31/2026, 5:29:05 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        numbers = {}
4        for i,n in enumerate(nums):
5
6            if target - n in numbers:
7                return [i , numbers[target-n] ]
8            
9            numbers[n] = i
10            
11