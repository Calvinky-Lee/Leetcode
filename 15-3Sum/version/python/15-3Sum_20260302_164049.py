# Last updated: 3/2/2026, 4:40:49 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        output = []
4        stored = {}
5        nums = sorted(nums)
6        for i in range(len(nums)):
7            stored[nums[i]] = i
8        
9        for i in range(len(nums)-1):
10            if i > 0 and nums[i] == nums[i-1]:
11                continue
12
13            for j in range(i+1, len(nums)):
14                if j > i+1 and nums[j] == nums[j-1]:
15                    continue
16                target = -(nums[i] + nums[j])
17                if target in stored and stored[target] > j:
18                    output.append([nums[i],nums[j],target])
19        
20        return output
21
22        