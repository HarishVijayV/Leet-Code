class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        count=1
        maxx=1
        for i in range(len(s)-1):
            if ord(s[i])+1==ord(s[i+1]):
                count+=1
                maxx=max(maxx,count)
            else:
                count=1
        return maxx