class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        count=0
        cc=0
        for i in range(len(nums)):
            c=bin(i)
            for j in c:
                if j=='1':
                    cc+=1
            if cc==k:
                count+=nums[i]
            cc=0
        return count