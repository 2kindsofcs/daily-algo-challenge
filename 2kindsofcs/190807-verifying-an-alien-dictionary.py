class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        wordCount = len(words)
        for i in range(wordCount-1):
            word1, word2 = words[i], words[i+1]
            smallerLength = min(len(word1), len(word2))
            if smallerLength == len(word2) and word1[:len(word2)] == word2:
                return False
            for j in range(smallerLength):
                if order.index(word1[j]) < order.index(word2[j]):
                    break
                elif order.index(word1[j]) == order.index(word2[j]):
                    continue
                return False 
        return True 
            
        
# Runtime: 44 ms, faster than 63.33% of Python3 online submissions for Verifying an Alien Dictionary.
# Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Verifying an Alien Dictionary.
