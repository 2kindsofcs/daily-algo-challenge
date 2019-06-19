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
                    # int 대신 ord로 아스키코드값을 얻어서 이용. 
                    # 0의 아스키코드값인 48을 빼주면 digit에 해당하는 수가 됨 
                    if currentNum % (ord(digit)-48) != 0:
                        result.pop()
                        break
            currentNum = currentNum + 1
        return result

# Runtime: 48 ms, faster than 93.41% of Python3 online submissions for Self Dividing Numbers.
# Memory Usage: 13.2 MB, less than 29.61% of Python3 online submissions for Self Dividing Numbers.
# string으로 만들었던 수를 int를 이용해 다시 수를 만드는 대신 ord를 이용. 속도가 좀 더 빨라졌다. 
