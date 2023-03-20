"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
https://leetcode.com/problems/valid-anagram/
"""
from collections import Counter


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:

    def is_anagram_with_sorting(self, s: str, t: str) -> bool:
        # not recommended
        # min time for sorting is O(nlog(n))
        return sorted(s) == sorted(t)

    def is_anagram_library(self, s: str, t: str) -> bool:
        # using library collections Counter
        return Counter(s) == Counter(t)

    def is_anagram_brute_force(self, s: str, t: str) -> bool:
        # brute force using hashmap
        # time O(n)
        # memory O(n)
        if len(s) != len(t): return False
        s_hashmap = self._is_anagram_brute_force_helper(s)
        t_hashmap = self._is_anagram_brute_force_helper(t)
        for letter in s_hashmap:
            try:
                t_hashmap[letter]
            except KeyError:
                return False
            if s_hashmap[letter] != t_hashmap[letter]:
                return False
        return True

    def _is_anagram_brute_force_helper(self, text: str) -> dict:
        hashmap = {}
        for letter in text:
            if letter in hashmap:
                hashmap[letter] += 1
            else:
                hashmap[letter] = 1
        return hashmap


    def is_anagram_brute_force_optimized(self, s: str, t: str) -> bool:
        # brute force using hashmap
        # time O(n)
        # memory O(n)
        if len(s) != len(t): return False
        s_hashmap = self._is_anagram_brute_force_helper_optimized(s)
        t_hashmap = self._is_anagram_brute_force_helper_optimized(t)
        for letter in s_hashmap:
            if s_hashmap[letter] != t_hashmap.get(letter, 0):
                return False
        return True

    def _is_anagram_brute_force_helper_optimized(self, text: str) -> dict:
        hashmap = {}
        for i in range(len(text)):
            hashmap[text[i]] = 1 + hashmap.get(text[i], 0)
        return hashmap


s = "anagram"
t = "nagaram"
solution = Solution()
print(solution.is_anagram_brute_force(s, t))
