class Solution:
    def digitSum(self, s: str, k: int) -> str:
        ans=''
        while len(s)>k:
            i=0
            while i<len(s):
                summ=sum(int(dig) for dig in s[i:i+k])
                ans+=str(summ)
                i+=k
            s=ans
            ans=''
        return s
        