class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2==0:
            x=['a']*(n-1)
            y=['b']*1
            x=''.join(x)
            y=''.join(y)
            c=x+y
            return c
        else:
            x=['a']*(n)
            x=''.join(x)
            return x
            

        