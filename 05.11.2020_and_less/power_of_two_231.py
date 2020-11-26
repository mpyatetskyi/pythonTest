# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        check = range((-2) ** 31, 2 ** 31 - 1)
        value = 2
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        while n > value:
            value = value * 2
        if n == value:
            return True
        if n != value:
            return False




