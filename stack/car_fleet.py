"""
There are n cars going to the same destination along a one-lane road.
The destination is target miles away.

You are given two integer array position and speed, both of length n,
where position[i] is the position of the ith car and speed[i] is the
speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it
and drive bumper to bumper at the same speed. The faster car will slow
down to match the slower car's speed. The distance between these two
cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position
and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point,
it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

https://leetcode.com/problems/car-fleet/
"""

from typing import List


class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = [(pos, s, (target-pos)/s) for pos, s in zip(position, speed)]
        data.sort(key=lambda x: x[0])
        stack = [data[-1]]
        for i in range(len(position)-2, -1, -1):
            if stack and stack[-1][2] < data[i][2]:
                stack.append(data[i])
        return len(stack)

    def carFleetIntuition(self, target, position, speed):
        data = [(pos, s) for pos, s in zip(position, speed)]
        data.sort(key=lambda x: x[0])
        count = 0

        while data:
            is_popped = False

            for i in range(len(data)):
                new_position = data[i][0] + data[i][1]
                data[i] = (new_position, data[i][1])

            while data and data[-1][0] >= target:
                data.pop()
                is_popped = True

            if is_popped:
                count += 1

        return count


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
solution = Solution()
print(solution.carFleet(target, position, speed))
