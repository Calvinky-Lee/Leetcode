# Last updated: 3/1/2026, 1:58:36 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        prefix = [0] * len(nums)
4        postfix = [0] * len(nums)
5        current = 1
6
7        #calculating for prefix
8        for i in range(len(nums)):
9            current *= nums[i]
10            prefix[i] =  current
11
12        
13        #calculating for postfix
14        current = 1
15        for i in range(len(nums)-1 ,-1, -1):
16            current *= nums[i]
17            postfix[i] = current
18
19        for i in range(len(nums)):
20            if i == 0:
21                nums[i] = postfix[i + 1]
22            elif i == len(nums) - 1:
23                nums[i] = prefix[i-1]
24            else:
25                nums[i] = prefix[i-1] * postfix[i+1]
26        
27        return nums