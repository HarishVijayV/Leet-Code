class Solution:
    def replaceDigits(self, s: str) -> str:
        s=list(s)
        for i in range(1,len(s),2):
            s[i]=shift(s[i-1],s[i])
        return ''.join(s)

def shift(a,b):
    return chr(ord(a)+int(b))