class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dictt1=defaultdict(int)
        dictt2=defaultdict(int)
        count=0
        for i in s:
            dictt1[i]+=1
        for i in t:
            dictt2[i]+=1
        for i in dictt1.keys():
            if dictt1[i]!=dictt2[i] and dictt1[i]>dictt2[i]:
                count+=dictt1[i]-dictt2[i]
        return count