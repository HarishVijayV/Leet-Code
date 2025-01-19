class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dictt=defaultdict(int)
        c=0
        ans=[]
        for i in nums:
            dictt[i]+=1
            ans.append(dictt[i])
        ma=max(ans)
        for i,j in dictt.items():
            if j==ma:
                c+=j
        return c
        

        