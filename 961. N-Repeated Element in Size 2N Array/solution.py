class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dictt=defaultdict(int)
        for i in nums:
            dictt[i]+=1
        for i,j in dictt.items():
            if j==len(nums)//2:
                return i
            