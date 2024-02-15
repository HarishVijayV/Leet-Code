class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<sum(nums[0:i]):
                return sum(nums[0:i+1])
        return -1

