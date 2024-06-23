class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages=[]
        n=len(nums)
        for i in range(n//2):
            a=min(nums)
            nums.remove(a)
            b=max(nums)
            nums.remove(b)
            ans=(a+b)/2
            averages.append(ans)
        return min(averages)
        