# Last updated: 2/4/2026, 12:16:10 PM
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {')':'(', ']':'[' , '}':'{' }
        stack = []
        for i in range(len(s)):
            if stack and bracket_dict.get(s[i]) == stack[-1]:
                    stack.pop(-1)
            else:
                stack.append(s[i])
        if len(stack) == 0:
            return True
        return False