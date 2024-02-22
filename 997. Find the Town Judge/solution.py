class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        dictt={}
        for i in trust:
            if i[1] in dictt:
                dictt[i[1]]+=1
            else:
                dictt[i[1]]=1
        for i ,j in dictt.items():
            if j==n-1 and i not in (k[0] for k in trust):
                return i
        return -1
 