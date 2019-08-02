"""
LeetCode : 169. Majority Element
problem : https://leetcode.com/problems/majority-element/
solution :
1. 집합에 넣어서 nums의 중복을 제거
2. 집합의 원소를 하나씩 빼내서 그 수가 절반 이상인 수가 나타나면 반환
"""

class Solution:
    def majorityElement(self, nums):
        nums_set = set(nums)
        half_count = len(nums) // 2
        for num in nums_set:
            if half_count < nums.count(num):
                print(num)
                return num
        return -1


s = Solution()
s.majorityElement([3,2,3])
s.majorityElement([2,2,1,1,1,2,2])



