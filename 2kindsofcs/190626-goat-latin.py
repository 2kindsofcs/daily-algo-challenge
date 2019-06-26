class Solution:
    def toGoatLatin(self, S: str) -> str:
        wordList = S.split(" ")
        vowelList = ["a", "e", "i", "o", "u"]
        goatwords = []
        for index, word in enumerate(wordList):
            if word[0].lower() in vowelList:
                word = word + "ma"
            elif len(word) > 1:
                word = word[1:] + word[0] + "ma"
            else:
                word = word + "ma"
            word = word + ("a" * (index + 1))
            goatwords.append(word)
        return " ".join(goatwords)
    
# Runtime: 36 ms, faster than 75.33% of Python3 online submissions for Goat Latin.
# Memory Usage: 13.1 MB, less than 83.58% of Python3 online submissions for Goat Latin.
