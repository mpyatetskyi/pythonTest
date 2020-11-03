# https://leetcode.com/problems/reformat-date/

class Solution:
    def reformatDate(self, date: str) -> str:
        monthes = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07",
                   "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

        date = date.split()
        day = date[0]
        daylen = len(day)
        month = monthes[date[1]]
        year = date[2]
        if daylen == 3:
            day = '0' + day[0]
        elif daylen == 4:
            day = day[:2]

        newdate = year + '-' + month + '-' + day
        return newdate