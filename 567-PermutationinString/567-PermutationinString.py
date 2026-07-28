# Last updated: 7/28/2026, 4:57:28 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
9        if p is None or q is None:
10            return (p is None) and (q is None)
11        else:
12            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
13        