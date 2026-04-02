# Last updated: 4/2/2026, 1:44:59 PM
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output = []
        stored = {}
        nums = sorted(nums)
        for i in range(len(nums)):
            stored[nums[i]] = i
        
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                target = -(nums[i] + nums[j])
                if target in stored and stored[target] > j:
                    output.append([nums[i],nums[j],target])
        
        return output

        