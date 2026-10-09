# Last updated: 10/9/2026, 2:57:37 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
8        dummy = ListNode(0, head)
9        beforeptr = dummy
10        nptr = dummy
11
12        for i in range(n):
13            nptr = nptr.next
14        
15        while nptr.next is not None:
16            beforeptr = beforeptr.next
17            nptr = nptr.next
18        
19        beforeptr.next = beforeptr.next.next
20
21        return dummy.next