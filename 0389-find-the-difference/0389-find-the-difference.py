class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dictt=defaultdict(int)
        for i in (s):
            dictt[i]+=1
        for i in t:
            dictt[i]-=1
        for i,j in dictt.items():
            if j==-1:
                return i
        