import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = math.floor(math.sqrt(area))
        if l * l == area:
            return [l, l]
        while l < area:
            l += 1
            if area % l == 0 and area % (area // l) == 0:
                return [l, area // l]

# Runtime: 1748 ms, faster than 5.38% of Python3 online submissions for Construct the Rectangle.
# Memory Usage: 13.6 MB, less than 5.00% of Python3 online submissions for Construct the Rectangle.
# hotsummer님 코드를 참고하여 바꿔보았는데, 코드 자체는 더 간결해진 것 같지만 메모리는 약간 덜 사용하고 속도는 배로 느려졌다.
# math.sqrt의 비용이 생각보다 비싼가? 그래도 이전 코드에 있던 abs()가 빠졌는데.
