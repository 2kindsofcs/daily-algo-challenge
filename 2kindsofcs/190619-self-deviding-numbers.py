# https://leetcode.com/problems/self-dividing-numbers

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        currentNum = left
        result = []
        while currentNum <= right:
            strNum = str(currentNum)
            if "0" in strNum:
                pass
            else:
                result.append(currentNum)
                for digit in strNum:
                    if currentNum % int(digit) != 0:
                        result.pop()
                        break
            currentNum = currentNum + 1
        return result


# Runtime: 52 ms, faster than 84.10% of Python3 online submissions for Self Dividing Numbers.
# Memory Usage: 13.2 MB, less than 53.75% of Python3 online submissions for Self Dividing Numbers.

# 생각해보니 중복되는 digit에 대해서는 계산할 필요가 없다. 

