class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dictt=defaultdict(int)
        listt=[]
        for i in nums:
            dictt[i]+=1
        for i,j in dictt.items():
            if j==2:
                listt.append(i)
        for i in range(1,len(nums)+1):
            if i not in nums:
                listt.append(i)
        return listt