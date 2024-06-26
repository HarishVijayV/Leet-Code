class Solution:
    def clearDigits(self, s: str) -> str:
        s=list(s)
        i=0
        while i < len(s):
            if s[i].isdigit():
                s.pop(i)
                i-=1
                for j in range(i,-1,-1):
                    if not s[j].isdigit():
                        s.pop(j)
                        i-=1
                        break
            i+=1
        return ''.join(s)


        