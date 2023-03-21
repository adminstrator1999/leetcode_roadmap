"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
https://leetcode.com/problems/group-anagrams/
"""
from typing import List
from collections import defaultdict


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        # time O(n*m)
        # memory O(n*m)
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch)-ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

    def group_anagrams_hashmap(self, strs: List[str]) -> List[List[str]]:
        # time O(n*mlogm) ish not sure though because elements inside the list matters
        # memory O(n*m)
        # besides we can use key as a tuple also like tuple(sorted(text)) it makes little difference
        hashmap = dict()
        for text in strs:
            key = "".join(sorted(text))
            hashmap[key] = [text] + hashmap.get(key, [])
        return list(hashmap.values())

    def group_anagrams_brute_force(self, strs: List[str]) -> List[List[str]]:
        # time  O(n^2)
        # memory O(n)
        sorted_strs = {"".join(sorted(text)) for text in strs}
        result = []
        for u_text in sorted_strs:
            temp = []
            for text in strs:
                if u_text == "".join(sorted(text)):
                    temp.append(text)
            result.append(temp)
        return result


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
solution.group_anagrams(strs)
