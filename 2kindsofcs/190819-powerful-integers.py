class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        def getMaxPower(number):
            maxPower = 0
            if number == 1:
                return number 
            while True: 
                if number ** maxPower < bound:
                    maxPower += 1
                    continue
                else:
                    break
            return maxPower
        xMaxPower = getMaxPower(x)
        yMaxPower = getMaxPower(y)
        answer = []
        for i in range(xMaxPower):
            number = x ** i
            for j in range(yMaxPower):
                result = number + (y ** j)
                if result <= bound and result not in answer:
                    answer.append(result)
        return answer
   

# Runtime: 36 ms, faster than 78.63% of Python3 online submissions for Powerful Integers.
# Memory Usage: 13.8 MB, less than 12.50% of Python3 online submissions for Powerful Integers.
