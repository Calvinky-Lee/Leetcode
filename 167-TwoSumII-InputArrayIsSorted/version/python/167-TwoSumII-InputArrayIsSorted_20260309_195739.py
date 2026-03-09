# Last updated: 3/9/2026, 7:57:39 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        right = len(numbers) - 1
4        left = 0
5
6        while left < right:
7            if numbers[left] + numbers[right] == target:
8                return [left+1,right+1]
9            elif numbers[left] + numbers[right] > target:
10                right -= 1
11            elif numbers[left] + numbers[right] < target:
12                left += 1
13
14
15
16