class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                continue
            else:
                c+=1
                if s[i-1]==' ':
                    return c
        return c