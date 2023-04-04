"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
https://leetcode.com/problems/trapping-rain-water/
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # time O(n)
        # memory O(1)
        if not height: return 0

        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        res = 0
        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                res += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                res += max_right - height[r]
        return res

    def trap_better_than_easy(self, height: List[int]) -> int:
        # time O(n)
        # memory O(1)
        l, r = 0, len(height) - 1
        max_left = 0
        max_right = 0
        ans = 0
        while l <= r:
            if max_left <= max_right:
                ans += max_left - height[l] if max_left - height[l] > 0 else 0
                if height[l] > max_left: max_left = height[l]
                l += 1
            else:
                ans += max_right - height[r] if max_right - height[r] > 0 else 0
                if height[r] > max_right: max_right = height[r]
                r -= 1
        return ans

    def trap_brute_force(self, height: List[int]) -> int:
        # time O(N)
        # memory O(n)
        size = len(height)
        max_left = [0] * size
        max_right = [0] * size
        min_left_right = []
        for i in range(size):
            if i - 1 >= 0:
                max_left[i] = height[i - 1] if height[i - 1] > max_left[i - 1] else max_left[i - 1]
            if size - i < size:
                max_right[size - 1 - i] = height[size - i] if height[size - i] > max_right[size - i] else max_right[
                    size - i]
        for l, r in zip(max_left, max_right):
            min_left_right.append(min(l, r))
        ans = 0
        for i in range(size):
            ans += min_left_right[i] - height[i] if min_left_right[i] - height[i] > 0 else 0
        return ans

    def trap_easy_solution(self, height: List[int]) -> int:
        # time O(n^2) ish
        # memory O(1)
        if len(height) == 1: return 0
        ans = 0
        l, r = -1, max(height)
        for i in range(len(height)):
            temp = min(l, r) - height[i]
            ans += 0 if temp < 0 else temp
            if height[i] > l:
                l = height[i]
            if height[i] == r:
                r = max(height[i + 1:]) if len(height[i + 1:]) > 0 else -1
        return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [1, 2, 3, 5, 2, 3, 1, 6, 1]
# height = [5, 3, 0, 4, 2, 3, 0]
solution = Solution()
print(solution.trap(height))
