"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

https://leetcode.com/problems/top-k-frequent-elements/
"""
from typing import List
from collections import defaultdict, Counter
import heapq


class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        # time O(1)
        if len(nums) == k: return nums

        # time O(n)
        count = Counter(nums)

        # time O(nlogm)
        return heapq.nlargest(k, count.keys(), key=count.get)

    def top_k_frequent_another_approach(self, nums: List[int], k: int) -> List[int]:
        # time complexity O(n)
        # memory O(n)
        # draw it for better visualization

        hashmap = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            hashmap[num] += 1

        for i, c in hashmap.items():
            freq[c].append(i)

        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

    def top_k_frequent_first_thought(self, nums: List[int], k: int) -> List[int]:
        # time O(nlogn)
        # memory O(n)
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        max_values = sorted(hashmap.values())[-k:]
        reverse_hashmap = {value: key for key, value in hashmap.items()}
        return [reverse_hashmap[value] for value in max_values]


nums = [1, 1, 1, 2, 2, 3]
k = 2
solution = Solution()
print(solution.top_k_frequent(nums, k))
