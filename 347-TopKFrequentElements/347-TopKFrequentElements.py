# Last updated: 4/2/2026, 1:44:49 PM
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        heap = []
        returnl = []
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 0
        
        for i in counts:
            heapq.heappush(heap, (-counts[i], i))

        for i in range(k):
            top = heapq.heappop(heap)
            returnl.append(top[1])
        
        return returnl
                    

