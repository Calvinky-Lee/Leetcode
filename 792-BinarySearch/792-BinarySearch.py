# Last updated: 4/2/2026, 1:44:44 PM
import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            midway = left + (right-left)//2
            if nums[midway] == target:
                return midway
            elif nums[midway] > target:
                right = midway - 1
            elif nums[midway] < target:
                left = midway + 1

        return -1
        