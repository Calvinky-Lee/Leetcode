# Last updated: 3/5/2026, 3:07:28 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        output = [0] * len(temperatures)
4        stack = []
5        for i in range(len(temperatures)):
6            while stack and temperatures[i] > temperatures[stack[-1]]:
7                index = stack.pop()    
8                output[index] = i - index
9            stack.append(i)
10    
11        return output
12
13
14        
15        