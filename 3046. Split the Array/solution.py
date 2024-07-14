class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        n=len(nums)
        c=0
        dictt=defaultdict(int)
        for i in nums:
            dictt[i]+=1
            if dictt[i]>2:
                return False
        for i, j in dictt.items():
            if j==2:
                c+=1
                if c>n/2:
                    return False
        return True
        
        