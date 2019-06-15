class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        result = []
        d_count = S.count("D")
        i, d = d_count + 1, d_count - 1
        result.append(d_count)
        for letter in S:
            if letter == "D":
                result.append(d)
                d -= 1
            else: # letter == "I"
                result.append(i)
                i +=1
        return result
            
