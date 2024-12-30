class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lis=[]
        ans=[]
        for i,j in enumerate(nums):
            lis.append((i,j))
        sor=sorted(lis,key=lambda x:x[1])
        for i in range(len(sor)):
            if sor[i][1]==target:
                ans.append(i)
        ans.sort()
        return ans
        
        

        