class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        leftsum = 0
        rightsum = sum(nums)
        idx_cur = 0
        
        while (idx_cur < len(nums)):
            rightsum -= nums[idx_cur]
            if leftsum == rightsum:
                return idx_cur
            else:
                leftsum += nums[idx_cur]
                idx_cur += 1
                    
        
        return -1 