class Solution:
    def binaryGap(self, N: int) -> int:
        bilist=[]
        if N==0:
            return
        while N!=1:
            if N%2==1:
                bilist.append(1)
            else:
                bilist.append(0)
            N=N//2
        bilist.append(1)
        flag=False
        a,b,di,i=0,0,0,0
        for i in range(len(bilist)):
            if flag:
                if bilist[i]==1:
                    b=i
                    if di<b-a:
                        di=b-a
                    b=0
                    flag=False
            if bilist[i]==1 and flag==False:
                a=i
                flag=True
        return di
