class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        c=0
        for i in range(0,len(nums),2):
            c+=nums[i]
        return c

        