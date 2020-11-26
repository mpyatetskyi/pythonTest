# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for a in range(0,len(grid)):
            for i in grid[a]:
                if i >= 0:
                    continue
                else:
                    count += 1
        return count