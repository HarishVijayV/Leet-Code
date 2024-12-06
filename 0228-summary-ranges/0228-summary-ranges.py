class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans=[]
        k=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if k!=nums[i-1]:
                    ans.append(f"{k}->{nums[i - 1]}")
                else:
                    ans.append(str(k))
                k=nums[i]
        if k != nums[-1]:
            ans.append(f"{k}->{nums[-1]}")
        else:
            ans.append(str(k))
        return ans



        