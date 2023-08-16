"""
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
https://leetcode.com/problems/min-stack/
"""


class MinStack:

    def __init__(self):
        # i want to save both value and minimum value till
        # this value in the stack
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack and self.stack[-1][1] < val:
            self.stack.append((val, self.stack[-1][1]))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
