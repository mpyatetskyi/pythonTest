# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        if 1 <= n <= 10 ** 5:
            n = list(str(n))
            mysum = 0
            mymultiply = 1
            for i in n:
                mysum = mysum + int(i)
            for i in n:
                mymultiply = mymultiply * int(i)
            return mymultiply - mysum
