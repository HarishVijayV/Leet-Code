class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        for i in range(1,x+1,1):
            if (i*i)<=x:
                prev=i
                continue
            else:
                return prev