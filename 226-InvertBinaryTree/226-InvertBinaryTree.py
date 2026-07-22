# Last updated: 7/22/2026, 2:25:06 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        if root is None:
10            return None
11        
12        new_root = TreeNode(root.val)
13
14        new_root.left = self.invertTree(root.right)
15        new_root.right = self.invertTree(root.left)
16        
17        return new_root
18        