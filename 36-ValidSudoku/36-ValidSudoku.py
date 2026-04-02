# Last updated: 4/2/2026, 1:44:58 PM
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(9):
            for c in range(9):
                if board[i][c] == ".":
                    continue
                if (board[i][c] in rows[i] or
                    board[i][c] in columns[c] or 
                    board[i][c] in squares[(i//3 , c//3)]):
                    return False
                columns[c].add(board[i][c])
                rows[i].add(board[i][c])
                squares[(i//3,c//3)].add(board[i][c])
        return True