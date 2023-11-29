class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        s2=sorted(s2)
        s11=True
        s22=True
        for i in range(len(s1)):
            if s1[i]<s2[i]:
                s11=False
            if s2[i]<s1[i]:
                s22=False
        return s11 or s22