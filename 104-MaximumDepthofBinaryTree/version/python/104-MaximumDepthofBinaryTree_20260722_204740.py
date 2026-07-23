# Last updated: 7/22/2026, 8:47:40 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        if root is None:
10            return 0
11        elif root.left is None:
12            return 1 + self.maxDepth(root.right)
13        elif root.right is None:
14            return 1 + self.maxDepth(root.left)
15        else:
16            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
17        