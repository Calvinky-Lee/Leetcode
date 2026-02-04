# Last updated: 2/4/2026, 12:16:04 PM
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()
        res = []
        for i, x in enumerate(nums):
            while q and q[0] <= i - k:
                q.popleft()
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            if i + 1 >= k:
                res.append(nums[q[0]])
        return res