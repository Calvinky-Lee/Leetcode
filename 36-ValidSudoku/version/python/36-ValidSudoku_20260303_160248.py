# Last updated: 3/3/2026, 4:02:48 PM
1class Solution(object):
2    def isValidSudoku(self, board):
3        """
4        :type board: List[List[str]]
5        :rtype: bool
6        """
7        columns = collections.defaultdict(set)
8        rows = collections.defaultdict(set)
9        squares = collections.defaultdict(set)
10
11        for i in range(9):
12            for c in range(9):
13                if board[i][c] == ".":
14                    continue
15                if (board[i][c] in rows[i] or
16                    board[i][c] in columns[c] or 
17                    board[i][c] in squares[(i//3 , c//3)]):
18                    return False
19                columns[c].add(board[i][c])
20                rows[i].add(board[i][c])
21                squares[(i//3,c//3)].add(board[i][c])
22        return True