class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        block = len(matrix[0]) - 1
        length = len(matrix)
        for i in range(1, length):
            if matrix[i][1:] != matrix[i-1][0:block]:
                return False
        return True
    

            
# Runtime: 96 ms, faster than 92.68% of Python3 online submissions for Toeplitz Matrix.
# Memory Usage: 14 MB, less than 7.14% of Python3 online submissions for Toeplitz Matrix.
# 8분
