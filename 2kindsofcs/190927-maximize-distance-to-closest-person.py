class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        length = len(seats)
        maxCount, count, index, startIndex = 0, 0, 0, 0
        counting = False
        for i in range(length):
            if seats[i] == 0:
                if not counting:
                    index = i
                    counting = True
                count += 1 
            else:
                counting = False
                if count >= maxCount:
                    maxCount = count
                    startIndex = index
                count = 0
            if counting and i == length - 1:
                if count >= maxCount:
                    maxCount = count
                    startIndex = index
        seat = maxCount / 2 if maxCount > 1 else 1
        if maxCount % 2 == 1 and seat != 1:
            seat += 0.5 
        endIndex = startIndex + maxCount - 1
        if endIndex == length - 1 or startIndex == 0:
            return maxCount
        return round(seat)
        
# [0,0,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0] 같은 테스트케이스를 통과하지 못함    
