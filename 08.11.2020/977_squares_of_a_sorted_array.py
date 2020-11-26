# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        mylist = [i*i for i in A]
        mylist.sort()
        return mylist