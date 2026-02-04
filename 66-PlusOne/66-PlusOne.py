# Last updated: 2/4/2026, 12:16:07 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        totalstr = ''
        output = []
        for i in digits:
            totalstr += str(i)
        totalstr = str(int(totalstr) + 1)

        for i in totalstr:
            output.append(int(i))

        return output

        