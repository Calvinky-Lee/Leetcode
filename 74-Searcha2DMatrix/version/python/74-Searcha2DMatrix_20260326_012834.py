# Last updated: 3/26/2026, 1:28:34 AM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        l = 0
4        r = len(matrix) - 1
5        while r >= l:
6            mid = (l+r)//2
7            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
8                for i in matrix[mid]:
9                    if i == target:
10                        return True
11                return False
12            elif target >= matrix[mid][-1]:
13                l = mid + 1
14            else:
15                r = mid - 1
16        return False
17
18        