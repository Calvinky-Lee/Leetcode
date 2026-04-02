# Last updated: 4/2/2026, 1:44:51 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        current = 1

        #calculating for prefix
        for i in range(len(nums)):
            current *= nums[i]
            prefix[i] =  current

        
        #calculating for postfix
        current = 1
        for i in range(len(nums)-1 ,-1, -1):
            current *= nums[i]
            postfix[i] = current

        for i in range(len(nums)):
            if i == 0:
                nums[i] = postfix[i + 1]
            elif i == len(nums) - 1:
                nums[i] = prefix[i-1]
            else:
                nums[i] = prefix[i-1] * postfix[i+1]
        
        return nums