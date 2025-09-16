class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        ans=len(set(candyType))
        return min(len(candyType)//2, ans)
        