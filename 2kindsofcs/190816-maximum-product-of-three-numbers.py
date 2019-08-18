class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        product = nums[-1] * nums[-2] * nums[-3]
        if nums[0] < 0 and nums[1] < 0:
            return max((nums[0] * nums[1] * nums[-1]), product)
        return product
        

# Runtime: 316 ms, faster than 63.41% of Python3 online submissions for Maximum Product of Three Numbers.
# Memory Usage: 15 MB, less than 6.67% of Python3 online submissions for Maximum Product of Three Numbers.
