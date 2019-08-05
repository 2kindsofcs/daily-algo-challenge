class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNum = 0
        redunNum = 0
        for bit in nums:
            if bit == 1:
                redunNum += 1
                if redunNum > maxNum:
                    maxNum = redunNum
            else:
                redunNum = 0
        return maxNum
        
# Runtime: 400 ms, faster than 81.39% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 14 MB, less than 5.13% of Python3 online submissions for Max Consecutive Ones.
