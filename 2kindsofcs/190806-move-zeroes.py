class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroCount = nums.count(0)
        if not nums or zeroCount == 0 :
            return
        length = len(nums)
        index = 0
        end = length - zeroCount
        for i in range(length):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1 
        for i in range(end, length):
            nums[i] = 0
        """
        Do not return anything, modify nums in-place instead.
        """
        
# Runtime: 60 ms, faster than 61.36% of Python3 online submissions for Move Zeroes.
# Memory Usage: 14.8 MB, less than 5.00% of Python3 online submissions for Move Zeroes.
