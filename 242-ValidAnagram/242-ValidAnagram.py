# Last updated: 2/4/2026, 12:16:03 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        anagram_dict = {}
        for i in s:
            if i in anagram_dict:
                anagram_dict[i] = anagram_dict[i] + 1
            else:
                anagram_dict[i] = 1
        
        for i in t:
            if i in anagram_dict:
                t = t[1:]
                anagram_dict[i] = anagram_dict[i] - 1
                if anagram_dict[i] == 0:
                    del anagram_dict[i]

        if t == '' and len(anagram_dict) == 0:
            return True
        return False