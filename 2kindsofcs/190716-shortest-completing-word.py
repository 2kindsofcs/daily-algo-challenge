class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate = licensePlate.lower()
        words.sort(key=len)
        letters = {}
        length = len(plate)
        for letter in plate:
            if letter in string.ascii_lowercase:
                if letter not in letters:
                    letters[letter] = 1
                else:
                    letters[letter] += 1  
        letterKey = letters.keys() 
        for index, word in enumerate(words):
            for letter in letterKey:
                if word.count(letter) < letters[letter]:
                    break
            else:
                return words[index]
            
# Runtime: 40 ms, faster than 97.47% of Python3 online submissions for Shortest Completing Word.
# Memory Usage: 13.5 MB, less than 5.47% of Python3 online submissions for Shortest Completing Word.

# 문제에서 잘못 이해한 부분이 있었다. licensePlate에 같은 글자가 여러 번 나올 수도 있다고 되어있는데,
# 연속된 알파벳이 나올 수도 있으며 이 연속된 알파벳은 따로 취급되어야 한다고 잘못 이해했다. ex) pp가 나오면 supper처럼 연속해서 들어가야 함
# 그저 단순히 같은 글자가 여러 번 나올 수도 있다는 것일 뿐이었다.
