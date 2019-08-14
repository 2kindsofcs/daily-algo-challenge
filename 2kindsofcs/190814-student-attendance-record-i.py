class Solution:
    def checkRecord(self, s: str) -> bool:
        absentNum = s.count("A")
        if absentNum > 1 or "LLL" in s:
            return False
        return True
    
    
# Runtime: 36 ms, faster than 70.46% of Python3 online submissions for Student Attendance Record I.
# Memory Usage: 13.8 MB, less than 11.11% of Python3 online submissions for Student Attendance Record I.
