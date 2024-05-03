class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        sum=0
        maxx=-100000
        for i in (nums):
            sum+=i
            maxx= max(maxx,sum)
            sum= max(0,sum)

        return maxx
        