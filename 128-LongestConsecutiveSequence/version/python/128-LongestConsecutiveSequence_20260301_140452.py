# Last updated: 3/1/2026, 2:04:52 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        num_set = set(nums)
4        longest = 0
5        for i in num_set:
6            if (i - 1) not in num_set:
7                sequence = 0
8                while (i + sequence) in num_set:
9                    sequence += 1
10                longest = max(longest, sequence)
11        return longest