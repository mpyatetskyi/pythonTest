# https://leetcode.com/problems/power-of-three/submissions/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        check = range((-2) ** 31, 2 ** 31 - 1)
        value = 3
        if n in check:
            if n == 1:
                return True
            if n % 2 == 0:
                return False
            while n > value:
                value = value*3
            if n == value:
                return True
            else:
                return False
        else:
            return False