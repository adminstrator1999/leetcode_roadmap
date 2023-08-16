"""
Given an integer x, return true if x is a palindrome, and false otherwise.
https://leetcode.com/problems/palindrome-number/
"""


class Solution:

    def is_palindrome(self, x: int) -> bool:
        # solving this without changing this into string
        if x < 0:
            return False
        reversed_x = 0
        temp_x = x
        while temp_x:
            reversed_x *= 10
            reversed_x += temp_x % 10
            temp_x //= 10
        return reversed_x

    def is_palindrome_bad(self, x: int) -> bool:
        # solving this without changing this into string
        if x < 0:
            return False
        numbers = []
        while x:
            numbers.append(x % 10)
            x //= 10
        end = len(numbers) - 1
        begin = 0
        while begin < end:
            if numbers[begin] != numbers[end]:
                return False
            end -= 1
            begin += 1
        return True

    def is_palindrome_brute_force(self, x: int) -> bool:
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


solution = Solution()
print(solution.is_palindrome(100))
