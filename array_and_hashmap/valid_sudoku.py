"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
https://leetcode.com/problems/valid-sudoku/
"""
import collections
from typing import List


class Solution:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        # time O(1)
        # memory O(81)
        rows, columns, squares = [collections.defaultdict(set) for _ in range(3)]
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                if (value in rows[r] or
                    value in columns[c] or
                    value in squares[(r//3, c//3)]):
                    return False
                rows[r].add(value)
                columns[c].add(value)
                squares[(r//3, c//3)].add(value)
        # we can just save elements and keys in list and then compare length of it to its set
        return True

    def is_valid_sudoku_brute_force(self, board: List[List[str]]) -> bool:
        # time is O(n^n)
        # memory O(1)
        for row in board:
            filtered_row = list(filter(lambda x: x != ".", row))
            if len(filtered_row) != len(set(filtered_row)):
                return False
        for i in range(9):
            column = [row[i] for row in board if row[i] != "."]
            if len(column) != len(set(column)):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                group = []
                for row in board[i: i + 3]:
                    for item in row[j: j + 3]:
                        if item != ".":
                            group.append(item)
                if len(group) != len(set(group)):
                    return False
        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
solution = Solution()
solution.is_valid_sudoku(board)
