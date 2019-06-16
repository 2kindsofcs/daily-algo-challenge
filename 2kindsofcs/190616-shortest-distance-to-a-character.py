class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        # C의 위치를 알아낸다
        length = len(S)
        indexList = []
        result = [ 0 for _ in range(length)]
        if S.count(C) == length:
            return result
        for i in range(length):
            if S[i] == C:
                indexList.append(i)
        # 처음부터 끝까지 훑으면서 가장 가까운 C 위치를 찾는다
        for i in range(length):
            diff = min([ abs(index - i) for index in indexList])
            result[i] = diff
        return result
    
# Runtime: 88 ms, faster than 28.86% of Python3 online submissions for Shortest Distance to a Character.
# Memory Usage: 13.2 MB, less than 70.03% of Python3 online submissions for Shortest Distance to a Character.
    
# abs가 비용이 많이 들고, 모든 C의 위치에 대해 계산하고 있기 때문에 비효율적.
# 어떻게 하면 현재 위치에서 앞뒤로 있는 C의 위치에 대해서만 계산할 수 있을까?
