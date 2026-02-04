# Last updated: 2/4/2026, 12:16:11 PM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        maxlen = 0
        substring = set()

        for right in range(len(s)):
            if s[right] not in substring:
                maxlen = max(maxlen, right-left + 1)
                substring.add(s[right]) 
            else:
                while s[right] in substring:
                    substring.remove(s[left])
                    left += 1
                substring.add(s[right])
                
        
        return maxlen