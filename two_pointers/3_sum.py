"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
 and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
https://leetcode.com/problems/3sum/
"""
from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 1 and num == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    temp = sorted([num, nums[l], nums[r]])
                    if temp not in res:
                        res.append(temp)
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

    def three_sum_some_thoughts(self, nums: List[int]) -> List[List[int]]:
        # time O(nlogn) + O(n^2) => O(n^2)
        # memory O(1) if sorting dont take extra space
        size = len(nums)
        nums.sort()
        res = []
        for i in range(size - 2):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            two_sum = self._two_sum(nums[i + 1:], -1 * nums[i])
            if two_sum:
                for j in two_sum:
                    j.append(nums[i])
                    res.append(j)
        return res

    def _two_sum(self, rest_nums, target) -> list:
        ans = []
        l, r = 0, len(rest_nums) - 1
        while l < r:
            s = rest_nums[l] + rest_nums[r]
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            elif s == target and sorted([rest_nums[l], rest_nums[r]]) not in ans:
                ans.append(sorted([rest_nums[l], rest_nums[r]]))
                l += 1
            l += 1
        return ans

    def three_sum_brute_force_optimized(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        size = len(nums)
        for i in range(size - 2):
            for j in range(i + 1, size - 1):
                if not (i >= 1 and nums[i] == nums[i - 1] or nums[i] > 0):
                    for k in range(j + 1, size):
                        s = sorted([nums[i], nums[j], nums[k]])
                        if sum(s) == 0 and s not in ans:
                            ans.append([nums[i], nums[j], nums[k]])
        return ans

    def three_sum_brute_force(self, nums: List[int]) -> List[List[int]]:
        # time O(n^n^n)
        # memory O(n^n)
        hashset = []
        size = len(nums)
        for f in range(size):
            for s in range(1, size):
                for t in range(2, size):
                    if f != s != t and f != t:
                        u_nums = tuple(sorted((f, s, t)))
                        if u_nums not in hashset:
                            hashset.append(u_nums)
        ans = []
        for i, j, k in hashset:
            if nums[i] + nums[j] + nums[k] == 0:
                temp = sorted([nums[i], nums[j], nums[k]])
                if temp not in ans:
                    ans.append(temp)
        return ans


nums = [-1, 0, 1, 2, -1, -4]
# [-4, -1, -1, 0, 1, 2, 3]
# nums = [0, 0, 0]
solution = Solution()
print(solution.three_sum(nums))
