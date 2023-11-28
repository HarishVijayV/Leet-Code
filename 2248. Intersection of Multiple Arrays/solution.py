class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        dictt=defaultdict(int)
        listt=[]
        for i in nums:
            for j in i:
                dictt[j]+=1
        for i,j in dictt.items():
            if j==len(nums):
                listt.append(i)
        return sorted(listt)