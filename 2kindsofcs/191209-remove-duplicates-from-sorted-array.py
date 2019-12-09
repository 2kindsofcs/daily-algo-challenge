class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        realIndex, checkIndex = 0, 1
        count = 1
        while realIndex < length and checkIndex < length:
            if nums[realIndex] == nums[checkIndex]:
                checkIndex += 1
                continue
            else:
                realIndex += 1
                nums[realIndex] = nums[checkIndex]
                count += 1
        del nums[count:]
        return count

# Runtime: 88 ms, faster than 86.41% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted Array.
# 6개월 전에 풀었던 문제인데, 어떻게 풀었는지 기억이 잘 나질 않아서 다시 풀어 보았다. 그때의 코드는 1880ms가 소요되었는데 지금은 88ms. 뿌듯하다.
                
