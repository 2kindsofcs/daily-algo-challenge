class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xorNum = bin(x ^ y)
        return str(xorNum).count("1")
        

# Runtime: 36 ms, faster than 78.07% of Python3 online submissions for Hamming Distance.
# Memory Usage: 13 MB, less than 84.26% of Python3 online submissions for Hamming Distance.
    
# 일단 떠오르는대로 금방 풀었는데 결과는 생각보다 괜찮다. 다만 코드가 좀 불친절한 것 같다. 