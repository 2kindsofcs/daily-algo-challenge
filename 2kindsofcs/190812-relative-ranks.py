class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        length = len(nums)
        medals = ["Bronze Medal", "Silver Medal", "Gold Medal"]
        sortedNums = sorted(nums)
        sortedNums.reverse() # reverse는 sort와 마찬가지로 return 하지 않는다 
        rankDic = {}
        if length <= 3:
            for num in sortedNums:
                rankDic[num] = medals.pop()
            return [ rankDic[num] for num in nums ]
        for num in sortedNums[0:3]:
            rankDic[num] = medals.pop()
        for i in range(3, length):
            rankDic[sortedNums[i]] = "{0}".format(i + 1)
        return [ rankDic[num] for num in nums ]

# Runtime: 84 ms, faster than 63.54% of Python3 online submissions for Relative Ranks.
# Memory Usage: 14.7 MB, less than 25.00% of Python3 online submissions for Relative Ranks.
# 첫번째~세번째 요소에 대한 처리가 중복되는데, 좀 더 간결하게 바꿀 수 없을까?
