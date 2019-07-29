# https://leetcode.com/problems/lemonade-change

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change5 = 0
        change10 = 0
        for bill in bills:
            if bill == 5:
                change5 += 1
            if bill == 10:
                if change5 == 0:
                    return False
                change10 += 1
                change5 -= 1
            if bill == 20:
                if change10 > 0:
                    if change5 > 0:
                        change10 -= 1
                        change5 -= 1
                    else:
                        return False
                elif change5 >= 3:
                    change5 -= 3
                else:
                    return False
        return True

# Runtime: 164 ms, faster than 69.57% of Python3 online submissions for Lemonade Change.
# Memory Usage: 14 MB, less than 5.71% of Python3 online submissions for Lemonade Change.
# if문이 지저분하다. 분명 개선의 여지가 있다. 
