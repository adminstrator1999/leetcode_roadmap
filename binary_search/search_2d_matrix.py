"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the
previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
https://leetcode.com/problems/search-a-2d-matrix/
"""

from typing import List


class Solution:

    def search(self, nums, target, is_2d=True):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if (nums[mid][0] if is_2d else nums[mid]) > target:
                right = mid - 1
            elif (nums[mid][-1] if is_2d else nums[mid]) < target:
                left = mid + 1
            else:
                return nums[mid]
        return "not_found"

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        data = self.search(matrix, target)
        print(data)
        if data == "not_found":
            return False
        res = self.search(data, target, is_2d=False)
        if res == "not_found":
            return False
        return True

    def searchMatrixIntuition(self, matrix: List[List[int]], target: int) -> bool:
        # this has some problems
        l, r = 0, len(matrix) - 1
        insider = 0
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                insider = matrix[m]
                break
        new_l, new_r = 0, len(insider) - 1
        while new_l <= new_r:
            new_m = (new_l + new_r) // 2
            if insider[new_m] > target:
                new_r = new_m - 1
            elif insider[new_m] < target:
                new_l = new_m + 1
            else:
                return True
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
solution = Solution()
print(solution.searchMatrix(matrix, target))
