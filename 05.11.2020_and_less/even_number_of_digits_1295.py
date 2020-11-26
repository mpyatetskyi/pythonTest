# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if int(len(str(num))) % 2 == 0:
                count += 1
            else:
                continue

        return count