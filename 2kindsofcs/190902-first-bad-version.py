# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        pivot, lower, upper = 1, 1, n
        if n < 4:
            for i in range(1, n + 1):
                if isBadVersion(i):
                    return i
        if isBadVersion(1):
            return 1
        if isBadVersion(n) and not isBadVersion(n-1):
            return n
        while True:
            pivot = round((upper + lower)/2)
            # 나쁜 버전이면 앞쪽 검사
            if isBadVersion(pivot):
                upper = pivot
                if not isBadVersion(pivot-1):
                    return pivot
            # 정상 버전이면 뒤쪽 검사 
            else:
                lower = pivot 
        return pivot 
    
# Runtime: 36 ms, faster than 64.76% of Python3 online submissions for First Bad Version.
# Memory Usage: 13.8 MB, less than 6.90% of Python3 online submissions for First Bad Version.
# 예외 처리가 지저분해서 마음에 들지 않는다.
                
