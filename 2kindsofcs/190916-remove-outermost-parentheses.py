class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        length = len(S)
        if length < 3:
            return ""
        parenStack, results = [], []
        label = 0
        for i in range(length):
            if S[i] == "(":
                parenStack.append(S[i])
            else:
                parenStack.pop()
            if not parenStack:
                results.append(S[label:i + 1])
                label = i + 1
        answer = ""
        for result in results:
            answer = answer + result[1:-1]
        return answer
        
# Runtime: 40 ms, faster than 91.11% of Python3 online submissions for Remove Outermost Parentheses.
# Memory Usage: 14.2 MB, less than 5.56% of Python3 online submissions for Remove Outermost Parentheses.
