"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
https://leetcode.com/problems/valid-palindrome/
"""
from curses.ascii import isalpha


class Solution:
    def is_palindrome(self, s: str) -> bool:
        def al_num(c):
            return (ord("A") <= ord(c) <= ord("Z") or
                    ord("a") <= ord(c) <= ord("z") or
                    ord("0") <= ord(c) <= ord("9"))

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not al_num(s[l]):
                l += 1
            while l < r and not al_num(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def is_palindrome_two_pointer(self, s: str) -> bool:
        # time O(n)
        # memory O(1)
        # not non-alphanumeric
        start, end = 0, len(s) - 1
        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

    def is_palindrome_brute_force(self, s: str) -> bool:
        # time O(n)
        # memory O(n)
        new_s = ""
        for n in s:
            if n.isalnum():
                new_s += n.lower()
        return new_s == new_s[::-1]


s = "a :abBaa9 "
solution = Solution()
print(solution.is_palindrome_brute_force(s))
