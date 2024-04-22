class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c=0
        for _ in range(len(nums)):
            if min(nums)>=k:
                return c
            else:
                nums.remove(min(nums))
                c+=1
        