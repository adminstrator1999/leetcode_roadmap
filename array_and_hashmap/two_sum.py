"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # while keeping track of numbers indices in hashmap,
        # we loop through the nums and if we find target-num we return
        # time O(n)
        # memory O(n)
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [i, hashmap[target-num]]
            hashmap[num] = i


