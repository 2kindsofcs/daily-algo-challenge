class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length <= 2:
            return max(nums)
        if length == 3:
            return max((nums[0] + nums[2]), nums[1])
        maxList = [ 0 for _ in range(length) ]
        maxList[0] = nums[0]
        maxList[1] = nums[1]
        maxList[2] = nums[0] + nums[2]
        for i in range(3, length):
            maxList[i] = nums[i] + max(maxList[i - 3], maxList[i - 2])
        return max(maxList[length - 2], maxList[length - 1])
    
    
# Runtime: 40 ms, faster than 49.57% of Python3 online submissions for House Robber.
# Memory Usage: 13.6 MB, less than 9.09% of Python3 online submissions for House Robber.
