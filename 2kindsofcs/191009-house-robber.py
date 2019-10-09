class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        def robMax(index, total):
            if index >= length:
                return total
            total += nums[index]
            return max(robMax(index + 2, total), robMax(index + 3, total))
        return max(robMax(0,0), robMax(1,0))
