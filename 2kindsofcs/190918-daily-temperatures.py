class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        T.append(0)
        answer = []
        for i in range(length):
            for j in range(i + 1, length):
                if T[j] > T[i]:
                    answer.append(j - i)
                    break
            else:
                answer.append(0)
        return answer 
        
# Time limit exceeded
