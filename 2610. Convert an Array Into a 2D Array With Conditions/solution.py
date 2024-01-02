class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dictt=defaultdict(int)
        for i in nums:
            dictt[i]+=1
        final=[]
        while max(dictt.values())>0:
            res=[]
            for i,j in dictt.items():
                if j>0:
                    res.append(i)
                    dictt[i]-=1
            final.append(res)
        return final



        