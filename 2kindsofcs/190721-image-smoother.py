import math
import copy
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        if M == []:
            return []
        width = len(M[0])
        length = len(M)
        row = 0
        N = copy.deepcopy(M)
        while row < length:
            for index, cell in enumerate(M[row]):
                adjacent = []
                if index > 0: 
                    adjacent.append(M[row][index-1])
                    if row < length - 1:
                        adjacent.append(M[row+1][index-1])
                if index < width - 1:
                    adjacent.append(M[row][index+1])
                    if row > 0:
                        adjacent.append(M[row-1][index+1])
                if row > 0:
                    adjacent.append(M[row-1][index])
                    if index > 0:
                        adjacent.append(M[row-1][index-1])
                if row < length - 1:
                    adjacent.append(M[row+1][index])
                    if index < width - 1:
                        adjacent.append(M[row+1][index+1])
                N[row][index] = math.floor((cell + sum(adjacent))/(1+len(adjacent)))
            row = row + 1
        return N
    
# Runtime: 752 ms, faster than 16.13% of Python3 online submissions for Image Smoother.
# Memory Usage: 14.7 MB, less than 5.13% of Python3 online submissions for Image Smoother.
# 일단 주변 8개의 셀에 대해서 판별하는 코드가 가독성이 매우 떨어지고, 속도도 느리고 메모리도 많이 소비하고 있다. 
# deepcopy를 사용하지 않는 방법은 없을까? 
