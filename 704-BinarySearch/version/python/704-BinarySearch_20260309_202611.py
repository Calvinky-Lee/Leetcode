# Last updated: 3/9/2026, 8:26:11 PM
1import math
2class Solution:
3    def search(self, nums: List[int], target: int) -> int:
4        left = 0
5        right = len(nums) - 1
6
7        while left <= right:
8            midway = left + (right-left)//2
9            if nums[midway] == target:
10                return midway
11            elif nums[midway] > target:
12                right = midway - 1
13            elif nums[midway] < target:
14                left = midway + 1
15
16        return -1
17        