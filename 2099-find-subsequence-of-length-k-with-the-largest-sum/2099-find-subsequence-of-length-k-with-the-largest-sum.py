class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        lis=[]
        for i,j in enumerate(nums):
            lis.append((i,j))
        a=sorted(lis, key=lambda x:x[1], reverse=True)
        topk=a[:k]
        sor=sorted(topk,key=lambda x:x[0])
        ans=[j[1] for j in sor]
        return ans