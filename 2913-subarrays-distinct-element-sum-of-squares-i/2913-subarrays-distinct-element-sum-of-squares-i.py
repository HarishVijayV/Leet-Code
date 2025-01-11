class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)):
            seen = set()
            for j in range(i, len(nums)):
                seen.add(nums[j]) 
                c += len(seen) * len(seen)  
        return c
