# Last updated: 4/3/2026, 3:15:26 PM
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