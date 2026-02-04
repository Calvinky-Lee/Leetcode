# Last updated: 2/4/2026, 12:16:02 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        track_dict = {}
        for i in nums:
            if i in track_dict:
                return True
            else:
                track_dict[i] = 1
        return False