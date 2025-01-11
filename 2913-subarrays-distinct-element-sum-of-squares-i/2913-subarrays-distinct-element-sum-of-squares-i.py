class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums),1):
                c+=len(set(nums))*len(set(nums))
        return c+len(nums)
            

            

