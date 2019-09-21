class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        length = len(T)
        result = [ 0 for _ in range(length) ]
        for i in range(length):
            while stack and T[i] > T[stack[-1]]:
                index = stack.pop()
                result[index] = i - index;
            stack.append(i)
        return result
                
# Runtime: 544 ms, faster than 57.21% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 17.4 MB, less than 13.16% of Python3 online submissions for Daily Temperatures.
# 온도가 지속적으로 감소할 경우 감소하는 것들을 저장해뒀다가 증가하게 될 경우 빠르게 처리할 수 있다. 
# 먼젓번 풀이의 경우 특히 지속적으로 감소하다가 거의 끝에서 증가할 경우 불필요한 연산을 굉장히 많이 하게 됨. 
# 각 온도의 입장에서 유의미한 높은 온도가 무엇인지를 아는 것이 포인트. 1 - 2 - 1 - 3- 5 - 7 이 있다고 하면 2 입장에서는 5, 7이 필요가 없음. 
# 3만 알면 됨. 그리고 3 입장에서는 제일 첫번째 1은 필요가 없음. 이미 2가 등장했었기 때문. 
# 무엇을 기억해야 하고 무엇을 기억할 필요가 없는지를 빠르게 파악하자.       
