# Last updated: 4/2/2026, 1:45:00 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxarea = 0 
        while right >= left:
            maxarea = max(maxarea, (right - left) * min(height[left], height[right]))
            #print(maxarea, right - left * min(height[left], height[right]))
            if height[right] > height[left]:
                left +=1
            else:
                right -= 1
        
        return maxarea



        