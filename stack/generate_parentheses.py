"""
Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses.
https://leetcode.com/problems/generate-parentheses/
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(left, right, s):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                dfs(left+1, right, s+"(")
            if right < left:
                dfs(left, right+1, s+")")
        dfs(0, 0, "")
        return res

    def generate_parentheses(self, n: int) -> List[str]:

        res = []
        stack = []

        def bactrack(open, close):
            if open == close == n:
                res.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                bactrack(open + 1, close)
                stack.pop()

            if close < open:
                stack.append(")")
                bactrack(open, close + 1)
                stack.pop()

        bactrack(0, 0)
        return res


solution = Solution()
print(solution.generate_parentheses(3))
