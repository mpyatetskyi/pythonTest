# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[:n+1]
        nums2 = nums[n:]
        nums3 = []
        for a,b in zip(nums1,nums2):
            nums3.append(a)
            nums3.append(b)
        return nums3