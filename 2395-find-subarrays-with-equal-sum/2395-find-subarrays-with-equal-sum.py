class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        k=nums[0]+nums[1]
        seen=[k]
        for i in range(1,len(nums)-1):
            if nums[i]+nums[i+1] in seen:
                return True
            else:
                seen.append(nums[i]+nums[i+1])
        return False
        