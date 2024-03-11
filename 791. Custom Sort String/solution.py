class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans=''
        s=list(s)
        for i in order:
            while i in s:
                ans+=i
                s.pop(s.index(i))
        return ans+''.join(s)
