import math

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        totalNum = len(candies)
        kindNum = len(set(candies))
        if kindNum >= totalNum/2:
            return math.floor(totalNum/2)
        else:
            return kindNum
   
# Runtime: 124 ms, faster than 39.25% of Python3 online submissions for Distribute Candies.
# Memory Usage: 14.7 MB, less than 62.96% of Python3 online submissions for Distribute Candies.
# 필요한 논리는 간단한데 짐짓 어렵게 생각해서 조금 헤맸다. 최대로 가질 수 있는 경우와 최소로 가질 수 있는 경우를 잘 생각해보면
# 논리 도출은 어렵지 않은 문제이다. 
