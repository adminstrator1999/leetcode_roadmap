"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
https://leetcode.com/problems/product-of-array-except-self/
"""
import copy
from typing import List
from functools import reduce


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        # time O(n)
        # memory O(1) if we don't count answer as an extra space
        size = len(nums)
        ans = [1 for _ in range(size)]
        pre, post = 1, 1
        for i in range(1, size):
            pre *= nums[i - 1]
            ans[i] = pre
        for i in range(size-2, -1, -1):
            post *= nums[i+1]
            ans[i] *= post
        return ans

    def product_except_self_extra_memory(self, nums: List[int]) -> List[int]:
        # memory is O(n)
        # time O(n)
        size = len(nums)
        prefix = []
        suffix = [0 for _ in range(size)]
        for i in range(size):
            if i == 0:
                prefix.append(nums[i])
            else:
                prefix.append(prefix[i - 1] * nums[i])
        for i in range(size - 1, -1, -1):
            if i == size - 1:
                suffix[i] = nums[i]
            else:
                suffix[i] = suffix[i + 1] * nums[i]
        ans = []
        for i in range(size):
            if i == 0:
                ans.append(suffix[i + 1])
            elif i == size - 1:
                ans.append(prefix[i - 1])
            else:
                ans.append(prefix[i - 1] * suffix[i + 1])
        return ans

    def product_except_self_using_division_optimized(self, nums):
        prod, zero_cnt = reduce(lambda a, b: a * (b if b else 1), nums, 1), nums.count(0)
        if zero_cnt > 1: return [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt:
                nums[i] = 0 if c else prod
            else:
                nums[i] = prod // c
        return nums

    def product_except_self_using_division(self, nums: List[int]) -> List[int]:
        # time is O(n)
        # memory is O(1)
        # if there is zero in list it is going to be problem here
        # there are a lot of edge cases here related to zero so not recommended
        if not any(nums):
            return nums
        product = 1
        zero = False
        for num in nums:
            if num == 0:
                zero = True
                product *= 1
            else:
                product *= num

        for i in range(len(nums)):
            if zero and nums[i] == 0:
                nums[i] = product
            elif zero and nums[i] != 0:
                nums[i] = 0
            else:
                nums[i] = int(product / nums[i])

        return nums

    def product_except_self_brute_force(self, nums: List[int]) -> List[int]:
        # time O(n^n)
        # memory O(n)
        # literally brute force
        def calculate_product(i: int, nums: List[int]):
            ans = 1
            for index in range(len(nums)):
                if index == i:
                    continue
                ans *= nums[index]
            return ans

        copy_array = copy.copy(nums)
        for i in range(len(nums)):
            nums[i] = calculate_product(i, copy_array)
        return nums


# nums = [1, 2, 3, 4]
# nums = [-1, 1, 0, -3, 3]
# nums = [0, 0]
nums = [0, 4, 0]

# Output: [24,12,8,6]
solution = Solution()
print(solution.product_except_self(nums))
