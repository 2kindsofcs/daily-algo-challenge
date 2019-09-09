class Solution:
    def findLHS(self, nums: List[int]) -> int:
        numsDic = {}
        result = 0
        for num in nums:
            if num not in numsDic:
                numsDic[num] = 1
            else:
                numsDic[num] += 1
            if (num + 1) in numsDic:
                result = max(result, (numsDic[num] + numsDic[num + 1]))
            if (num - 1) in numsDic:
                result = max(result, (numsDic[num] + numsDic[num - 1]))
        return result 
            
# Runtime: 440 ms, faster than 11.66% of Python3 online submissions for Longest Harmonious Subsequence.
# Memory Usage: 15.3 MB, less than 7.69% of Python3 online submissions for Longest Harmonious Subsequence.
                
