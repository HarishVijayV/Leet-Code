class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x=sorted(set(x for x,y in points))
        maxx=0
        for i in range(1,len(x),1):
            maxx=max(maxx,x[i]-x[i-1])
        return maxx

