# https://leetcode.com/problems/self-dividing-numbers

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        currentNum = left
        result = []
        while currentNum <= right:
            result.append(currentNum)
            quotient = currentNum
            digit = currentNum % 10
            while quotient:
                if digit == 0 or currentNum % digit != 0:
                    result.pop()
                    break
                quotient = quotient // 10
                digit = quotient % 10
            currentNum = currentNum + 1
        return result
    
# Runtime: 44 ms, faster than 98.03% of Python3 online submissions for Self Dividing Numbers.
# Memory Usage: 13.1 MB, less than 61.09% of Python3 online submissions for Self Dividing Numbers.

# 확실히 str()을 사용하지 않으니 속도, 메모리양 모두 향상되었다. 
