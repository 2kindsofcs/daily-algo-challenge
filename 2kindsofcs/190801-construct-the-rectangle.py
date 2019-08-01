class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        diff = 10000000
        answer = [area, 1]
        for i in range(1, area+1):
            if i ** 2 > area:
                break
            if area % i == 0:
                counterpart = area // i
                if abs(i - counterpart) < diff:
                    diff = abs(i - counterpart)
                    answer[0] = max(i, counterpart)
                    answer[1] = min(i, counterpart)
        return answer

# Runtime: 40 ms, faster than 63.01% of Python3 online submissions for Construct the Rectangle.
# Memory Usage: 13.7 MB, less than 6.52% of Python3 online submissions for Construct the Rectangle.
# 소수에 대한 계산을 따로 뺄 수도 있지 않을까 싶기는 한데, 일단은 그냥 떠오르는대로 풀어보았다. 
