"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
https://leetcode.com/problems/longest-consecutive-sequence/
"""
from typing import List


class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        # time O(n)
        # memory O(n)
        numSet = set(nums)
        longest = 0
        for num in nums:
            # check if num is the beginning of the sequence
            if num - 1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

    def longest_consecutive_set(self, nums: List[int]) -> int:
        # time O(n)
        # memory O(n)
        if len(nums) == 0: return 0
        nums = set(nums)
        begin = []
        for num in nums:
            if num - 1 not in nums:
                begin.append(num)
        l_count = 1
        for n in begin:
            count = 1
            curr = n
            while curr + 1 in nums:
                count += 1
                curr += 1
                l_count = max(l_count, count)
            else:
                continue
        return l_count

    def longest_consecutive_brute_force(self, nums: List[int]) -> int:
        # time O(n + nlogn)
        # memory O(1)
        if len(nums) == 0: return 0
        # need to delete duplicates which can hinder our logic
        nums = list(set(nums))
        max_count = 1
        curr_count = 1
        nums.sort()
        curr_val = nums[0]
        for num in nums[1:]:
            if num == curr_val + 1:
                curr_count += 1
                curr_val = num
                if curr_count > max_count:
                    max_count = curr_count
            else:
                curr_count = 1
                curr_val = num
        return max_count


nums = [-6]

solution = Solution()
print(solution.longest_consecutive(nums))
