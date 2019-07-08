class Solution:
    def calPoints(self, ops: List[str]) -> int:
        pointSum = 0
        lastIndex = -1
        validCounts = []
        symbols = ["C", "D", "+"]
        for index, point in enumerate(ops):
            if point not in symbols and type(int(point)) == type(0):
                validCounts.append(int(point))
                pointSum = pointSum + int(point)
                lastIndex = lastIndex + 1 
            if point == "C":
                pointSum = pointSum - validCounts.pop()
                lastIndex = lastIndex - 1 
            if point == "+":
                lastTwoSum = validCounts[lastIndex] + validCounts[lastIndex - 1]
                validCounts.append(lastTwoSum)
                pointSum = pointSum + lastTwoSum
                lastIndex = lastIndex + 1
            if point == "D":
                lastDouble = validCounts[lastIndex] * 2
                validCounts.append(lastDouble)
                pointSum = pointSum + lastDouble
                lastIndex = lastIndex + 1 
        return pointSum
                
                
# Runtime: 36 ms, faster than 79.22% of Python3 online submissions for Baseball Game.
# Memory Usage: 13.3 MB, less than 28.64% of Python3 online submissions for Baseball Game

# 처음에 포인터 세 개 만들어서 풀었다가 잘못 풀었음을 알고 다시 풀었다. 좀 더 깔끔하게 정리할 수 있을 것 같다. 
