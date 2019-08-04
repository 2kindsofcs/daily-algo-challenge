class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 1 or not nums:
            return []
        nums.sort()
        redun = 0
        for i in range(length-1):
            if nums[i] == nums[i+1]:
                redun = nums[i]
        missedNum = list(set([i for i in range(1, length+1)]) - set(nums))[0]
        return [redun, missedNum]
        
# Runtime: 268 ms, faster than 17.82% of Python3 online submissions for Set Mismatch.
# Memory Usage: 16.3 MB, less than 5.45% of Python3 online submissions for Set Mismatch.
# 일단 떠오르는 대로 풀었다. 다시 고칠 필요 있음. 
