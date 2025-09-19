class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a=sum(nums)
        nn=0
        while True:
            if a%k==0:
                return nn
            else:
                nn+=1
                a-=1
        return 0
                


        