# Last updated: 3/4/2026, 3:42:25 PM
1import string
2class Solution:
3    def isPalindrome(self, s: str) -> bool:
4        nonchar = 0
5        s = s.lower()
6        allowed = set(string.ascii_lowercase + string.digits)
7
8        cleaned = []
9        for ch in s:
10            if ch in allowed:
11                cleaned.append(ch)
12        s = "".join(cleaned)
13
14
15        left = 0
16        right = len(s) - 1
17
18        while (right > left):
19            if s[right] != s[left]:
20                return False
21            left += 1
22            right -= 1
23        return True
24            
25            
26
27
28        