"""
Given an integer x, return true if x is a palindrome, and false otherwise.
https://leetcode.com/problems/palindrome-number/
"""

class Solution:
    def is_palindrome(self, x: int) -> bool:
        # brute force approach
        # convert into string and use two pointers
        string_x = str(x)
        length = len(string_x)
        end = length - 1 
        begin = 0 
        while begin < end:
            if string_x[begin] != string_x[end]:
                return False
            end -= 1
            begin += 1
        return True