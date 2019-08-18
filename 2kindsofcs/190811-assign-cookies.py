class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g의 각 요소들과 같거나 더 큰 숫자가 s에 몇 개나 있느냐? 
        g.sort()
        s.sort()
        gLength, sLength = len(g), len(s)
        indexS, indexG, count = 0, 0, 0
        while indexG < gLength and indexS < sLength:
            if s[indexS] >= g[indexG]:
                count += 1
                indexG += 1
            indexS += 1 
        return count 
    
# Runtime: 188 ms, faster than 97.01% of Python3 online submissions for Assign Cookies.
# Memory Usage: 15.4 MB, less than 14.29% of Python3 online submissions for Assign Cookies.
# while문 조건이 저게 최선인가? 
