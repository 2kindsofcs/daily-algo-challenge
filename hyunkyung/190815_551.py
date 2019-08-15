class Solution:
    def checkRecord(self, s: str) -> bool:
        ct=0
        i=0
        flag=True
        for i in range(len(s)):
            if s[i]=="A":
                ct+=1
                if ct>=2:
                    flag=False
                    break
            elif s[i]=="L":
                if i+2<len(s):
                    if s[i+1]=="L" and s[i+2]=="L":
                        flag=False
                        break
                else:
                    continue
        return flag
