class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {1:1, 2:2, 3:3}
        count = 0     
        def countWays(num):
            if num in dic:
                return dic[num]
            dic[num - 1] = countWays(num - 1)
            dic[num - 2] = countWays(num - 2)
            return dic[num - 1] + dic[num - 2]
        return countWays(n)

# Runtime: 28 ms, faster than 98.20% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.9 MB, less than 5.97% of Python3 online submissions for Climbing Stairs.
# 12분
