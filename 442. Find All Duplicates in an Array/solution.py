class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dictt=defaultdict(int)
        lis=[]
        for i in nums:
            dictt[i]+=1
        for i ,j in dictt.items():
            if j>1:
                lis.append(i)
        return lis