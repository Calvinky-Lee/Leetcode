# Last updated: 10/12/2026, 4:38:16 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        self.result = 0
10
11        def dfs(tree):
12            if not tree:
13                return 0
14            
15            left = dfs(tree.left)
16            right = dfs(tree.right)
17
18            self.result = max(self.result, right + left)
19            return 1 + max(left, right)
20            
21        dfs(root)
22        return self.result
23
24
25        