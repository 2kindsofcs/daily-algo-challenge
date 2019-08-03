class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half = len(nums) / 2
        numDic = {}
        for num in nums:
            if num not in numDic:
                numDic[num] = 1
            else:
                numDic[num] += 1
            if numDic[num] > half:
                return num 
            
# Runtime: 200 ms, faster than 51.10% of Python3 online submissions for Majority Element.
# Memory Usage: 15 MB, less than 5.14% of Python3 online submissions for Majority Element.
