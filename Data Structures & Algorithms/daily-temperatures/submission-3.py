from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        
        for i in range(n):
            temp = temperatures[i]
            if (stack and stack[-1][0] > temp) or not stack:
                stack.append((temp, i))
                continue
            while stack and stack[-1][0] < temp:
                lowerTemp = stack.pop()
                j = lowerTemp[1]
                res[j] = i - j
            stack.append((temp, i))

        return res

            



        



