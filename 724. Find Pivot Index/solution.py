class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum=0
        rsum=sum(nums)
        for i in range(len(nums)):
            if lsum==rsum-nums[i]:
                return i
            else:
                lsum+=nums[i]
                rsum-=nums[i]
        return -1
        
        