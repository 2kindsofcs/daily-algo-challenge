"""
LeetCode : 492. Construct the Rectangle
Problem : https://leetcode.com/problems/construct-the-rectangle/
Conditions :
 - W <= L, L과 W의 차가 가능한 적어야 한다.
 - W * L이 area가 나와야 한다.
Solution :
직관적으로 W의 최대값은 area의 제곱근보다 작거나 같은 정수임을 유추할 수 있다.
W의 최대값을 구하고, area에서 W를 나눈 값이 0이 되는지 확인한다(W*L이 area인지 확인하는 것이다)
아닐 경우 w의 값을 줄여주면서 조건이 맞는지 확인하고, 맞으면 해당 값을 반환한다.
"""
import math

class Solution:
    def constructRectangle(self, area: int):
        w = int(math.sqrt(area))
        while 0 < w:
            if area % w == 0:
                l = area // w
                return [l, w]
            w -= 1

s = Solution()
s.constructRectangle(4)
s.constructRectangle(1)
s.constructRectangle(27)
s.constructRectangle(30)
