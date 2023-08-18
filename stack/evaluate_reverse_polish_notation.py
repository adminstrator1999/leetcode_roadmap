"""
You are given an array of strings tokens that represents an arithmetic
 expression in a Reverse Polish Notation.

Evaluate the expression.
Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression
in a reverse polish notation.
The answer and all the intermediate calculations
can be represented in a 32-bit integer.
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""


from typing import List


class Solution:

    def subtract(self, a, b):
        return a - b

    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        return int(a / b)

    def multiply(self, a, b):
        return a * b

    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"-": self.subtract,
                    "+": self.add,
                    "*": self.multiply,
                    "/": self.divide}
        stack = []
        for token in tokens:
            if token in operands:
                b = stack.pop()
                a = stack.pop()
                stack.append(operands[token](a, b))
            else:
                stack.append(int(token))
        return stack[0]
