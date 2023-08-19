"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature. If there is no future
day for which this is possible, keep answer[i] == 0 instead.
https://leetcode.com/problems/daily-temperatures/
"""


from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((temp, i))
        return res

    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        # this is way to long time
        res = []
        for i in range(len(temperatures)):
            count = 0
            add_zero = True
            for t in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[t]:
                    res.append(count + 1)
                    add_zero = False
                    break
                else:
                    count += 1
            if add_zero:
                res.append(0)
        return res


solution = Solution()
print(solution.dailyTemperatures([73, 74, 75, 71, 69, 70, 76, 73]))
