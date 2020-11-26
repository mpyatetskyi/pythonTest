class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target in nums:
            return nums.index(target)
        if not target in nums:
            for i in nums:
                if i < target:
                    continue
                if i > target:
                    ind = nums.index(i) - 1
                    break
            return ind