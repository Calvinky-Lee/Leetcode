# Last updated: 3/21/2026, 7:25:10 PM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        l = 0
4        r = len(matrix) - 1
5        while r >= l:
6            mid = (l+r)//2
7            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
8                for i in matrix[mid]:
9                    print(i)
10                    if i == target:
11                        return True
12                return False
13            elif target >= matrix[mid][-1]:
14                l = mid + 1
15            else:
16                r = mid - 1
17
18        return False
19
20        