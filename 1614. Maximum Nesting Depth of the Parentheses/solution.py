class Solution:
    def maxDepth(self, s: str) -> int:
        l=0
        r=0
        max=-1
        for i in s:
            if i=='(':
                l+=1
            elif i==')':
                r+=1
            if l-r>max:
                max=l-r
        return max
        