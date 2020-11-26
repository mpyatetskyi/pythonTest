# https://leetcode.com/problems/running-sum-of-1d-array/submissions/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newlist = []
        for a,num in enumerate(nums):
            newlist.append(sum(nums[:a+1]))
        return newlist