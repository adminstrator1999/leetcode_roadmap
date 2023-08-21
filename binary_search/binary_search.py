"""
Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
https://leetcode.com/problems/binary-search/
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2  # or we can do left+(right-left)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

    def search_intuition(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            half = (begin + end) // 2
            if nums[half] > target:
                end = half - 1
            elif nums[half] < target:
                begin = half + 1
            else:
                return half
        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 3
solution = Solution()
print(solution.search(nums, target))
