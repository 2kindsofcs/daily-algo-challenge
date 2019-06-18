class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xorNum = bin(x ^ y)
        return xorNum[2:].count("1")
        
# Runtime: 32 ms, faster than 91.93% of Python3 online submissions for Hamming Distance.
# Memory Usage: 13.1 MB, less than 60.69% of Python3 online submissions for Hamming Distance.
    
# bin 메소드의 리턴값은 스트링이다.