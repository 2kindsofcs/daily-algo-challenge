class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # S를 읽으면서 한글자씩 stack에 넣음. 
        # 만약 #이 나오면, stack이 비어있을 경우엔 그대로 둠
        # 만약 stack에 내용물이 있을 경우 pop함 
        # T에 대해서도 동일하게 진행
        # 두 스택을 같은지 비교. 
        stackS, stackT = [], []
        for letter in S:
            if letter != "#":
                stackS.append(letter)
            else:
                if stackS:
                    stackS.pop()
        for letter in T:
            if letter != "#":
                stackT.append(letter)
            else:
                if stackT:
                    stackT.pop()
        return stackS == stackT

# Runtime: 44 ms, faster than 9.20% of Python3 online submissions for Backspace String Compare.
# Memory Usage: 13.9 MB, less than 8.00% of Python3 online submissions for Backspace String Compare.
