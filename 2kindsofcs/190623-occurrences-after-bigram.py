class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = []
        isFirst, isSecond = False, False
        index = 0
        wordList = text.split(" ")
        length = len(wordList)
        if length < 3:
            return []
        while index < length-2:
            if wordList[index] == first and wordList[index+1] == second:
                result.append(wordList[index+2])
            index = index + 1
        return result
                
# Runtime: 36 ms, faster than 50.42% of Python3 online submissions for Occurrences After Bigram.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Occurrences After Bigram.
# 두 단어가 연속으로 나오는지 뒤에서 세 번째 단어까지 확인.
# 메모리는 다른 참가자 대비 적게 사용하는 듯 한데, 속도를 향상시킬 순 없을까?
            
