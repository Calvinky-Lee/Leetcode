# Last updated: 10/9/2026, 1:34:44 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: ListNode | None) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11
12        Element = head
13
14        if Element.next == None:
15            return head
16
17        Element2 = head.next        
18        Progress = head
19
20        while Element2 and Element2.next:
21            while Progress.next.next is not None:
22                Progress = Progress.next
23            
24            Element.next = Progress.next
25            Element.next.next = Element2
26            Progress.next = None
27
28            Element =  Element.next.next
29            Element2 = Element2.next
30            Progress = Element2
31        