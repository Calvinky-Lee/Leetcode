# Last updated: 2/4/2026, 12:16:06 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for i in num_set:
            if (i - 1) not in num_set:
                sequence = 0
                while (i + sequence) in num_set:
                    sequence += 1
                longest = max(longest, sequence)
        return longest
                