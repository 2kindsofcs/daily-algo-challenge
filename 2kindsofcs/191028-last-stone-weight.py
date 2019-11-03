class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:    
        while len(stones) > 1:
            max1 = max(stones)
            index1 = stones.index(max1)
            max1 = stones.pop(index1)
            max2 = max(stones)
            index2 = stones.index(max2)
            max2 = stones.pop(index2)
            if max1 - max2 != 0:
                stones.append(max(max1-max2, max2-max1))
        return stones[0] if stones else 0
    
    
# Runtime: 36 ms, faster than 83.91% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.
# 6분 7초
