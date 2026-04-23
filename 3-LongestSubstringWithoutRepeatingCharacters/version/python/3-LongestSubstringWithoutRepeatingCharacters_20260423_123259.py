# Last updated: 4/23/2026, 12:32:59 PM
1class Solution(object):
2    def lengthOfLongestSubstring(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        left = 0
8        maxlen = 0
9        substring = set()
10
11        for right in range(len(s)):
12            if s[right] not in substring:
13                maxlen = max(maxlen, right-left + 1)
14                substring.add(s[right]) 
15            else:
16                while s[right] in substring:
17                    substring.remove(s[left])
18                    left += 1
19                substring.add(s[right])
20                
21        
22        return maxlen