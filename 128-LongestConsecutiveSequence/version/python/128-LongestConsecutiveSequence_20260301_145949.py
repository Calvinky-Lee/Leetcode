# Last updated: 3/1/2026, 2:59:49 PM
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0] * n
        stack = []  # stores indexes

        for i in range(n):

            # resolve colder previous days
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev

            stack.append(i)

        return result