class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rowLength = len(grid[0])
        columnLength = len(grid)
        rl = rowLength + 2
        cl = columnLength + 2
        orangeList = [ 0 for i in range(rl * cl) ]
        # 0으로 된 padding을 포함하여 0으로 가득 찬 그리드를 만든다
        # 본값을 적절한 범위에 넣어준다
        # while True로 rotten 사방에 있는 애들을 rotting으로 표기
        # 필요한 변수는 round 횟수, rotten 개수, fresh 개수 
        # 맨 마지막에 rotting을 rotten으로 변경 
        # rotten 개수 업데이트. 이전 rotten과 업데이트할 rotten 개수가 동일하면
        # fresh가 있는지 체크, 있으면 -1, 없으면 라운드 수 리턴        
        for i in range(1, cl - 1):
            for j in range((i * rl) + 1, (i * rl) + rl - 1):
                orangeList[j] = grid[i - 1][j - (i * rl + 1)]
        if 1 not in orangeList:
            return 0
        roundCount, rottenCount, freshCount = 0, 0, 0
        totalLength = len(orangeList)
        while True:
            for i in range(totalLength):
                if orangeList[i] == 1:
                    if orangeList[i - rl] == 2 or orangeList[i + rl] == 2 or orangeList[i - 1] == 2 or orangeList[i + 1] == 2:
                        orangeList[i] = 3
            for i in range(totalLength):
                if orangeList[i] == 3:
                    orangeList[i] = 2
            newRotten = orangeList.count(2)
            freshCount = orangeList.count(1)
            if newRotten == rottenCount:
                if freshCount > 0:
                    return -1
                else:
                    return roundCount
            rottenCount = newRotten
            roundCount += 1 
            
# Runtime: 64 ms, faster than 42.57% of Python3 online submissions for Rotting Oranges.
# Memory Usage: 13.8 MB, less than 16.67% of Python3 online submissions for Rotting Oranges.
# 새롭게 썩은 오렌지가 있는지 boolean으로 저장해서 관리하면 답이 0인 케이스 처리가 깔끔해질 듯.
