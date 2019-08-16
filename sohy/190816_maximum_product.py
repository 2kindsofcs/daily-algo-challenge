class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        ret = 1
        if length < 3:
            return 0
        else:
            nums.sort(reverse = True)
            return max(nums[0]*nums[1]*nums[2], nums[length-1]*nums[length-2]*nums[0])
        
        
    '''
    Runtime: 236 ms, faster than 85.78% of Python online submissions for Maximum Product of Three Numbers.
    Memory Usage: 12.3 MB, less than 100.00% of Python online submissions for Maximum Product of Three Numbers.
    
    - redo [ ]
    - logic: first three, but if theres negative numbers, last two and one positive number. 
    - strategy: think of multiple dif situations 
        - [1]
        - [3,2,1]
        - [4,3,2,1,-3]
        - [4,3,-2,-1,-3]
    '''
