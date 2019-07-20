class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        if N == 1:
            return [1]
        if paths == []:
            return [1 for i in range(N)]
        gardenDic = {}
        flowers = [1,2,3,4]
        for path in paths:
            if path[0]-1 not in gardenDic:
                gardenDic[path[0]-1] = []
            if path[1]-1 not in gardenDic:
                gardenDic[path[1]-1] = []
        answer = [ 0 for i in range(N)]
        for group in paths:
            if group[1]-1 not in gardenDic[group[0]-1]:
                gardenDic[group[0]-1].append(group[1]-1)
            if group[0]-1 not in gardenDic[group[1]-1]:
                gardenDic[group[1]-1].append(group[0]-1)
        for garden in gardenDic:
            adjFlower = []
            adjacent = gardenDic.get(garden)
            for member in adjacent:
                if answer[member] not in adjFlower:
                    adjFlower.append(answer[member])
            for flower in flowers:
                if flower not in adjFlower:
                    answer[garden] = flower
        for i in range(N):
            if answer[i] == 0:
                answer[i] = 1
        return answer
        
# Runtime: 532 ms, faster than 5.06% of Python3 online submissions for Flower Planting With No Adjacent.
# Memory Usage: 20.4 MB, less than 100.00% of Python3 online submissions for Flower Planting With No Adjacent.

# 억지로 겨우 풀었다. 일단 풀었으니 개선할 방법을 고민해야겠다. 
