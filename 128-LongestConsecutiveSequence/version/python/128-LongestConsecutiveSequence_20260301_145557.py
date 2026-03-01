# Last updated: 3/1/2026, 2:55:57 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        output = [0] * len(temperatures)
4        stack = []
5        for i in range(len(temperatures)):
6            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
7                output[stack[-1]] = i - stack[-1]
8                stack.pop()
9        
10            stack.append(i)
11
12        
13        return output
14
15
16        
17        