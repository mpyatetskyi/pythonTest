# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        controllist = [0]

        if len(nums) <= 1:
            return False

        elif len(nums) > 1:
            for num in nums:
                if num in controllist:
                    return True
                if not num in controllist:
                    controllist.pop()
                    controllist.append(num)
            return False

