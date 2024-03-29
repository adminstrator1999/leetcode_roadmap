"""
Koko loves to eat bananas. There are n piles of bananas,
the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k.
Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will
not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all
the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas
within h hours.

https://leetcode.com/problems/koko-eating-bananas/
"""

from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        begin, end = 1, max(piles)
        res = end
        while begin <= end:
            mid = begin + (end - begin) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h:
                res = min(res, mid)
                end = mid - 1
            else:
                begin = mid + 1
        return res


piles = [3, 6, 7, 11]
h = 8
solution = Solution()
print(solution.minEatingSpeed(piles, h))
