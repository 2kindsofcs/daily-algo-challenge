class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 3:
            return -1 
        nums.append(0)
        leftSum = 0
        rightSum = sum(nums)
        for i in range(0, length):
            rightSum = rightSum - nums[i]
            if leftSum == rightSum:
                return i
            else:
                leftSum = leftSum + nums[i]
        return -1
    
# Runtime: 172 ms, faster than 81.94% of Python3 online submissions for Find Pivot Index.
# Memory Usage: 15.1 MB, less than 8.33% of Python3 online submissions for Find Pivot Index.

