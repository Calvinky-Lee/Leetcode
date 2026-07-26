# Last updated: 7/25/2026, 11:14:34 PM
1class Solution(object):
2    def climbStairs(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        memory = {}
8
9        for i in range(1,n+1):
10            if i == 1:
11                memory[i] = 1
12            elif i == 2:
13                memory[i] = 2
14            else:
15                memory[i] = memory[i-1] + memory[i-2]
16
17        return memory[n]