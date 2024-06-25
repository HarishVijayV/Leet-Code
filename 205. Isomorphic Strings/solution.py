class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictt={}
        dictn={}
        for i,j in zip(s, t):
            if i in dictt:
                if dictt[i]!=j:
                    return False
            if j in dictn:
                if dictn[j]!=i:
                    return False
            dictt[i]=j
            dictn[j]=i
        return True
                