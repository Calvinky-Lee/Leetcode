# Last updated: 4/2/2026, 1:44:57 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        left = 0
        right = len(height) - 1
        trapped = 0

        maxLeft = height[left]
        maxRight = height[right]

        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                trapped += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                trapped += maxRight - height[right]
            
        return trapped

        