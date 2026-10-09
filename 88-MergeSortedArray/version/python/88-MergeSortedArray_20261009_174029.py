# Last updated: 10/9/2026, 5:40:29 PM
1class Solution:
2    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        m_indx = m - 1
7        n_indx = n - 1
8        r_indx = m + n - 1
9
10        while n_indx >= 0:
11            if m_indx >= 0 and nums2[n_indx] < nums1[m_indx]:
12                nums1[r_indx] = nums1[m_indx]
13                m_indx -= 1
14                r_indx -= 1
15            else:
16                nums1[r_indx] = nums2[n_indx]
17                n_indx -= 1
18                r_indx -= 1
19
20
21
22
23        # first we need to iterate through all of nums1 
24        # from there stopping at each index if the nums2 position is less than = to nums1[i]
25        # it must be slotted in at nums1[i] and pop the 0 from the end then remove the element at the beggining of nums2. 
26
27        #if there is leftover in nums2 after this initial loop is done then pop nums1 len(nums2) times and append every element in nums2 into 
28
29
30        # left = 0
31        # while left < len(nums1) - 1 and nums1[left] < nums1[left + 1]:
32        #     while len(nums2) > 0 and nums2[0] >= nums1[left] and nums2[0] <= nums1[left + 1]:
33        #         nums1.insert(left + 1, nums2[0])
34        #         nums1.pop(-1)
35        #         nums2.pop(0)
36        #     left += 1
37
38        # for i in range(len(nums2)):
39        #     nums1.pop(-1)
40        # for i in range(len(nums2)):
41        #     nums1.append(nums2[i])