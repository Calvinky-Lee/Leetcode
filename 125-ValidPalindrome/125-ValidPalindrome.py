# Last updated: 4/2/2026, 1:44:55 PM
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        nonchar = 0
        s = s.lower()
        allowed = set(string.ascii_lowercase + string.digits)

        cleaned = []
        for ch in s:
            if ch in allowed:
                cleaned.append(ch)
        s = "".join(cleaned)


        left = 0
        right = len(s) - 1

        while (right > left):
            if s[right] != s[left]:
                return False
            left += 1
            right -= 1
        return True
            
            


        