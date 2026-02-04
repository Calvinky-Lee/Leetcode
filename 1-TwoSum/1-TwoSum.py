# Last updated: 2/4/2026, 12:16:15 PM
class Solution(object):
    def twoSum(self, nums, target):
        accum = {}
        for i, number in enumerate(nums):
            if target - nums[i] in accum:
                return [i, accum[target-nums[i]]]
            else:
                accum[number] = i
        

        