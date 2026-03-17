# Last updated: 3/17/2026, 12:03:46 AM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        l = 0
4        count = {}
5        result = 0
6
7        for r in range(len(s)):
8            count[s[r]] = 1 + count.get(s[r], 0)
9
10            while (r - l + 1) - max(count.values()) > k:
11                count[s[l]] -= 1
12                l += 1
13
14            result = max(result, r - l + 1)
15        return result
16    