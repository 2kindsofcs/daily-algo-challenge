class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        twoSum = m + n
        nums1[m:twoSum] = nums2
        if len(nums1) > twoSum:
            del num1[twoSum:]
        nums1.sort()

# Runtime: 32 ms, faster than 94.68% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.
