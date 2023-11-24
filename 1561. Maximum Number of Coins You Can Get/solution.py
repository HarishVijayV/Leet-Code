class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n=len(piles)//3
        sum=0
        a=sorted((piles))
        k=-2
        while n :
            sum+=a[k]
            k=k-2
            n=n-1
        return sum
