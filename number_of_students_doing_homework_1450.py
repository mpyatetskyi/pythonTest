# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for a,b in zip(startTime,endTime):
            if a <= queryTime <= b:
                count += 1
            else:
                pass
        return count