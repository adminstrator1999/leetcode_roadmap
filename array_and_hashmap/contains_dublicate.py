from typing import List

"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
https://leetcode.com/problems/contains-duplicate/
"""


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        # hashmap
        # for num in nums:
        #     if num in hashmap:
        #         hashmap[num] += 1
        #     else:
        #         hashmap[num] = 1
        # time O(n)
        # memory O(n)
        hashmap = {num: 0 for num in nums}
        return len(hashmap) != len(nums)

    def contains_duplicate_brute_force(self, nums: List[int]) -> bool:
        # brute force -> not recommended
        # Time O(n*n)
        # memory O(1)
        size = len(nums)
        if size == 0 or size == 1: return True
        for i in range(size - 1):
            for j in range(i + 1, size):
                if nums[i] == nums[j]:
                    return True
        return False

    def contains_duplicate_using_set(self, nums: List[int]) -> bool:
        # easy solution check if length of nums equals to length of set of nums
        # time(O(n))
        # memory(O(n))
        return len(nums) != len(set(nums))

    def check_if_all_answers_is_same(self, nums: List[int]) -> bool:
        return self.contains_duplicate_using_set(nums) == self.contains_duplicate(
            nums) == self.contains_duplicate_brute_force(nums)


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
solution = Solution()
print(solution.check_if_all_answers_is_same(nums))
