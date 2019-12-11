class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Length = len(nums1)
        nums2Length = len(nums2)
        if m == 0:
            for i in range(nums2Length):
                nums1[i] = nums2[i]
            if m > n:
                del nums1[n:]
        else:
            nums1[nums2Length:(nums2Length * 2)] = nums2
            nums1.sort()

            
# 제한 시간 끝에서야 문제가 잘못되어 있다는 것을 깨달았다. 
# 문제 설명이 잘못되어 있는 게 아쉽긴 하지만 그래도 풀어보는 것으로.
