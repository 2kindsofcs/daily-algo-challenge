class Solution:
    def isHappy(self, n: int) -> bool:
        squareList = []
        numString = str(n)
        while True:
            total = 0
            for bit in numString:
                total += (ord(bit) - 48) ** 2 
            if total not in squareList and total != 1:
                squareList.append(total)
                numString = str(total)
                continue
            if total in squareList:
                return False
            else:
                return True

# Runtime: 36 ms, faster than 90.07% of Python3 online submissions for Happy Number.
# Memory Usage: 13.1 MB, less than 79.73% of Python3 online submissions for Happy Number.
