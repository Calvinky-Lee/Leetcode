# Last updated: 3/5/2026, 3:39:57 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        left = 0
4        right = len(height) - 1
5        maxarea = 0 
6        while right >= left:
7            maxarea = max(maxarea, (right - left) * min(height[left], height[right]))
8            #print(maxarea, right - left * min(height[left], height[right]))
9            if height[right] > height[left]:
10                left +=1
11            else:
12                right -= 1
13        
14        return maxarea
15
16
17
18        