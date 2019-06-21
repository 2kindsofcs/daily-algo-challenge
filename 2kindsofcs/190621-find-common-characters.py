class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        index, result, countDic = 1, [], {}
        wordTotal = len(A)
        if A:
            for letter in A[0]:
                countDic[letter] = A[0].count(letter)
        while index < wordTotal:
            word = A[index]
            for letter in countDic:
                if word.count(letter) != 0:
                    countDic[letter] = min(countDic[letter], word.count(letter))
                else:
                    countDic[letter] = 0
            index += 1
        for letter in countDic:
            for _ in range(countDic[letter]):
                result.append(letter)
        return result

# Runtime: 56 ms, faster than 70.54% of Python3 online submissions for Find Common Characters.
# Memory Usage: 13.3 MB, less than 42.57% of Python3 online submissions for Find Common Characters.

# 생각해보니 countDic[letter] = 0을 쓰는 게 아니라 아예 딕셔너리에서 제거하고 싶은데, 그러면 interation 도중 countDic의 size가 변해 
# 에러가 생긴다. 뭔가 더 효율적인 방법은 없을까? 
