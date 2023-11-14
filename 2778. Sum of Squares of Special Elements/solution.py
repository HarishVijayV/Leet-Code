class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum=0
        n=len(nums)
        i=1
        while i<=n:
            if n%i==0:
                sum+=nums[i-1]*nums[i-1]
            i+=1
        return sum