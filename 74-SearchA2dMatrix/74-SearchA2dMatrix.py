# Last updated: 4/2/2026, 1:44:56 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while r >= l:
            mid = (l+r)//2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                for i in matrix[mid]:
                    if i == target:
                        return True
                return False
            elif target >= matrix[mid][-1]:
                l = mid + 1
            else:
                r = mid - 1
        return False

        