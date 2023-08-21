"""
Given an array of integers heights representing the histogram's bar height
where the width of each bar is 1, return the area of the largest rectangle
in the histogram.

https://leetcode.com/problems/largest-rectangle-in-histogram/
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # index, height
        max_area = 0
        for i, height in enumerate(heights):
            start_i = i
            while stack and stack[-1][1] > height:
                temp_i, temp_h = stack.pop()
                max_area = max(max_area, (i - temp_i) * temp_h)
                start_i = temp_i
            stack.append((start_i, height))
        length = len(heights)
        while stack:
            i, height = stack.pop()
            max_area = max(max_area, (length - i) * height)
        return max_area

heights = [2,1,5,6,2,3]
# heights = [5, 5, 3, 4, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
solution = Solution()
print(solution.largestRectangleArea(heights))
