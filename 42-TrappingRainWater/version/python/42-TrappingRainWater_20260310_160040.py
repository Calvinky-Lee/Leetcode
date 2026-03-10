# Last updated: 3/10/2026, 4:00:40 PM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        if len(height) == 0:
4            return 0
5
6        left = 0
7        right = len(height) - 1
8        trapped = 0
9
10        maxLeft = height[left]
11        maxRight = height[right]
12
13        while left < right:
14            if maxLeft < maxRight:
15                left += 1
16                maxLeft = max(maxLeft, height[left])
17                trapped += maxLeft - height[left]
18            else:
19                right -= 1
20                maxRight = max(maxRight, height[right])
21                trapped += maxRight - height[right]
22            
23        return trapped
24
25        