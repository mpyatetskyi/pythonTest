# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        myvalue = high - low
        if low%2 == 0 and high%2 == 0:
            myvalue = myvalue/2
        elif low%2 != 0 and high%2 == 0 or low%2 == 0 and high%2 != 0:
            myvalue = (myvalue+1)/2
        elif low%2 != 0 and high%2 != 0:
            myvalue = (myvalue/2) + 1
        return int(myvalue)