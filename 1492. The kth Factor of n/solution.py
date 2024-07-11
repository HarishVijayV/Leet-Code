class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ans=-1
        c=0
        i=1
        lis=[]
        while(i<=n):
            if n%i==0:
                c+=1
                lis.append(i)
            if c==k:
                return lis[-1]
            i+=1
        return -1
        