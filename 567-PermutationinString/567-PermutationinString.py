# Last updated: 7/28/2026, 5:38:19 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        output = [[]]
4        while nums != []:
5            adder = nums[0]
6            for i in range(len(output)):
7                new_add = output[i][:]
8                new_add.append(adder)
9                output.append(new_add)
10            nums.pop(0)
11        return output