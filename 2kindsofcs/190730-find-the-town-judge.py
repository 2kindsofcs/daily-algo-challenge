class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # 모든 사람이 Judge를 신뢰해야 함. 
        # Judge는 trust[0]에 등장하지 않음
        # town judge를 믿는 사람은 N - 1명이어야 함. 
        # twon judge를 믿는 사람이 N - 1명이고 그가 trustelement의 [0]에 등장하지 않아야 함 
        people = [ i for i in range (1, N+1) ]
        for relation in trust:
            if relation[0] in people:
                people.remove(relation[0])
        if len(people) != 1:
            return -1 
        townJudge = people.pop()
        count = 0
        for relation in trust:
            if relation[1] == townJudge:
                count += 1
        if count == N - 1:
            return townJudge
        return -1
        
# Runtime: 904 ms, faster than 13.67% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 18.3 MB, less than 10.00% of Python3 online submissions for Find the Town Judge.
# for문을 한번만 돌릴 수는 없을까? 
