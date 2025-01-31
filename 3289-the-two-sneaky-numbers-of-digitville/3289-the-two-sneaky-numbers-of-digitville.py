class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        lis=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                lis.append(nums[i])
        return lis
