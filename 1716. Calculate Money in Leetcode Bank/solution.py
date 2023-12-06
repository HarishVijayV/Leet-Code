class Solution:
    def totalMoney(self, n: int) -> int:
        k=0
        sum=0
        if n<=7:
            return n*(n+1)//2
        for i in range(7,n+1,7):
            sum+=28+7*k
            k+=1
        a=n%7
        c=(a*(a+1)//2)+k*a
        return c +sum
