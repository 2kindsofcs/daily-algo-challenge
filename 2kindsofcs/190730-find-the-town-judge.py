# 모든 사람이 Judge를 신뢰해야 함. 
# Judge는 trust[0]에 등장하지 않음
# town judge를 믿는 사람은 N - 1명이어야 함. 
# twon judge를 믿는 사람이 N - 1명이고 그가 trustelement의 [0]에 등장하지 않아야 함 


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        peopleTemp = { i for i in range(1, N + 1) }
        peopleList = [ 0 for i in range(1, N + 1) ]
        for relation in trust:
            peopleTemp.discard(relation[0])
            peopleList[relation[1] - 1] += 1
        if len(peopleTemp) == 1:
            townJudge = peopleTemp.pop()
            if peopleList[townJudge - 1] == N - 1:
                return townJudge
        return -1

# Runtime: 844 ms, faster than 62.79% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 18.4 MB, less than 10.00% of Python3 online submissions for Find the Town Judge.
# 어떻게 하면 메모리를 적게 사용할 수 있을까? 이런 저런 방법을 시도해봐도 계속 18.4~18.5MB.
