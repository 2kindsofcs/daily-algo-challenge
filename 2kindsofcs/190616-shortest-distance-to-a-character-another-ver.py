class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        length = len(S)
        indexList = []
        resultL = [ 0 for _ in range(length) ]
        resultR = [ 0 for _ in range(length) ]
        result = [ 0 for _ in range(length) ]
        if S.count(C) == length:
            return result
        # C의 위치들을 알아낸다
        for i in range(length):
            if S[i] == C:
                indexList.append(i)
        indexCount = len(indexList)
        index = -1
        # 왼편에서 가장 가까운 C 기준으로만 거리 계산
        for i in range(length):
            if i < indexList[index]:
                resultL[i] = float('inf')
            if S[i] == C:
                resultL[i] = 0
                index = index + 1
            if i > indexList[index]:
                resultL[i] = i - indexList[index]
        index = 0 
        # 오른편에서 가장 가까운 C 기준으로만 거리 계산
        for i in range(length):
            if S[i] == C and index != indexCount - 1:
                index = index + 1
            if i < indexList[index]:
                resultR[i] = indexList[index] - i
            if i > indexList[index]:
                resultR[i] = float('inf')
        # 위에서 구한 두 리스트에서 각각 더 작은 값을 취함
        for i in range(length):
            result[i] = min(resultL[i], resultR[i])
        return result

# Runtime: 48 ms, faster than 91.22% of Python3 online submissions for Shortest Distance to a Character.
# Memory Usage: 13.1 MB, less than 73.67% of Python3 online submissions for Shortest Distance to a Character.  

# 비슷한 게 반복되는 구조여서 맘에 들지 않는다. 
