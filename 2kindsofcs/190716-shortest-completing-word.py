class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate = licensePlate.lower() + "0"
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        letters = {}
        length = len(plate)
        index, leftPointer, rightPointer = 0, 0, 0
        flag = False
        if length == 1:
            rightPointer = 0 
        while index < length:
            if plate[index] in alphabets:
                if not flag:
                    leftPointer = index
                    rightPointer = leftPointer + 1
                if plate[leftPointer] != plate[rightPointer]:
                    if plate[index] not in letters:
                        letters[plate[index]] = 1
                    else:
                        letters[plate[index]] += 1
                    if rightPointer - leftPointer > 1:
                        redunStr = plate[leftPointer] * (rightPointer - leftPointer - 1)
                        if redunStr not in letters:
                            letters[redunStr] = 1
                        else:
                            letters[redunStr] += 1
                        flag = False
                else:
                    flag = True
                    rightPointer = rightPointer + 1
            index = index + 1    
        minLength = 16 
        wordIndex = 0 
        letterKey = letters.keys() 
        for index, word in enumerate(words):
            for letter in letterKey:
                if word.count(letter) < letters[letter]:
                    break
            else:
                length = len(word)
                if length < minLength:
                    minLength = length
                    wordIndex = index 
        return words[wordIndex]
            
# Runtime: 44 ms, faster than 93.66% of Python3 online submissions for Shortest Completing Word.
# Memory Usage: 13.3 MB, less than 40.84% of Python3 online submissions for Shortest Completing Word.  
# 푸는 데 시간도 엄청 오래 걸렸고, 코드도 지저분하다. 뭔가 더 단순한 해결 방법이 있는데 찾지 못하고 있는 건 아닌지?
