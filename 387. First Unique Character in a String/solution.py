class Solution:
    def firstUniqChar(self, s: str) -> int:
        lis=[]
        dictt=defaultdict(int)
        for i in s:
            dictt[i]+=1
        for i,j in dictt.items():
            if j==1:
                lis.append(i)
        for i in range(len(s)):
            if s[i] in lis:
                return i
        return -1
        

        