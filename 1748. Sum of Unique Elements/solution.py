class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dictt=defaultdict(int)
        count=0
        for i in nums:
            dictt[i]+=1
        for i,j in dictt.items():
            if j==1:
                count+=i
        return count