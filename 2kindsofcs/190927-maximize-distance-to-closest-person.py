class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        length = len(seats)
        left, right = [length] * length, [length] * length
        for i in range(length):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i - 1] + 1 
        for i in range(length - 1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < length - 1:
                right[i] = right[i + 1] + 1
        # if not seat --> 0을 false로 취급하므로 seat가 0인 경우만 체크하게 됨
        return max(min(left[i], right[i]) for i, seat in enumerate(seats) if not seat)
    
    
# Runtime: 164 ms, faster than 40.70% of Python3 online submissions for Maximize Distance to Closest Person.
# Memory Usage: 14.4 MB, less than 8.33% of Python3 online submissions for Maximize Distance to Closest Person.
# 딱 한 번만 순회해서 풀고 싶었는데, 그렇게 풀 경우 자잘한 예외처리를 너무 많이 해줘야해서 코드가 쓸데없이
# 복잡해지는 단점이 있었다. 이 쪽이 두 번 순회하지만 몹시 간결하고 이해가 잘 되기 때문에 더 나은 듯.
