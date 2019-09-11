import sys

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        # append를 쓰지 않고 구현해보고 싶었는데 잘 되질 않는다 
        self.stack.append(x)

    def pop(self) -> None:
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # min()을 쓰고싶지 않아서 간단하게 만들어 보았다 
        min = sys.maxsize
        for num in self.stack:
            if num < min:
                min = num
        return min
        

# Runtime: 1660 ms, faster than 5.06% of Python3 online submissions for Min Stack.
# Memory Usage: 17.6 MB, less than 5.36% of Python3 online submissions for Min Stack.
