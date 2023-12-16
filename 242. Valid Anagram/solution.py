class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictt1=defaultdict(int)
        for i in s:
            dictt1[i]+=1
        for i in t:
            if i in s:
                dictt1[i]-=1
            else:
                return False
        for i,j in dictt1.items():
            if j<=-1 or j>0:
                return False
        return True


        