# Last updated: 8/5/2026, 4:16:25 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        if not list1:
9            return list2
10        if not list2:
11            return list1
12            
13        if list1.val <= list2.val:
14            list1.next = self.mergeTwoLists(list1.next, list2)
15            return list1
16        else:
17            list2.next = self.mergeTwoLists(list1, list2.next)
18            return list2
19
20
21
22
23
24