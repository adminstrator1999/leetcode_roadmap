"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
https://leetcode.com/problems/container-with-most-water/
"""
from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

    def max_area_first_thought(self, height: List[int]) -> int:
        # time O(n)
        # memory O(1)
        x = len(height) - 1
        s = 0
        l, r = 0, x
        while l < r:
            if height[l] > height[r]:
                s = max(s, height[r] * x)
                r -= 1
            else:
                s = max(s, height[l] * x)
                l += 1
            x -= 1
        return s

    def max_area_brute_force(self, height: List[int]) -> int:
        # time O(n^2)
        # memory O(1)
        s = 0
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])
                s = max(s, area)
        return s


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
solution = Solution()
print(solution.max_area(height))
