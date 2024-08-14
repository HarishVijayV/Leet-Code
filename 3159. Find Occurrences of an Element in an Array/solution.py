class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        ans=[]
        anss=[]
        for i in range(len(nums)):
            if nums[i]==x:
                ans.append(i)
        for i in queries:
            if i<=len(ans):
                anss.append(ans[i-1])
            else:
                anss.append(-1)
        return anss