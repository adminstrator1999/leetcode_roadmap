"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for item in s:
            if item in pairs:
                if stack and stack[-1] == pairs[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        return not stack
