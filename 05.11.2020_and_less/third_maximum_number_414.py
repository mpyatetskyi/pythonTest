# https://leetcode.com/problems/third-maximum-number/
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = list(dict.fromkeys(nums))

        unique.sort(reverse=True)

        if len(unique) < 3:
            return unique[0]
        else:
            return unique[2]