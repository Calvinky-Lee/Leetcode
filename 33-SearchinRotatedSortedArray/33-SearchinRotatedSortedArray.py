# Last updated: 7/23/2026, 5:21:00 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        low = 0
4        high = len(nums) -1 
5
6        while low <= high:
7            mid = low + (high - low) // 2
8            print(mid, nums[mid], low, high)
9            if nums[mid] == target:
10                return mid
11            if nums[low] <= nums[mid]:
12                if nums[low] <= target < nums[mid]:
13                    high = mid - 1
14                else:
15                    low = mid + 1
16            else:
17                if nums[mid] < target <= nums[high]:
18                    low = mid + 1
19                else:
20                    high = mid - 1
21        return -1