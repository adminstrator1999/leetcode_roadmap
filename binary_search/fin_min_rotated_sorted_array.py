"""
Suppose an array of length n sorted in ascending order is rotated between 1
and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements,
return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid
        if nums[right] > nums[left]:
            return nums[0]
        return nums[right]
    
    def find_min(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res


# [2, 3, 4, 5, 6, 7, 0, 1]
solution = Solution()
print(solution.findMin([2, 3, 4, 5, 6, 7, 0, 1]))
