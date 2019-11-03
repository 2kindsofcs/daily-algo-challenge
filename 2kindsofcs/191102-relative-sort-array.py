class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        for num in arr2:
            dic[num] = arr1.count(num)
        keyList = dic.keys()
        result = []
        for num in keyList: 
            result.extend([num] * dic[num])
            for i in range(dic[num]):
                arr1.remove(num)
        arr1.sort()
        result.extend(arr1)
        return result
    
# Runtime: 52 ms, faster than 31.96% of Python3 online submissions for Relative Sort Array.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Relative Sort Array.
# 6분
