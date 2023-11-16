class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        listt=[]
        for i in nums:
            listt.append(i)
        listt=set(listt)
        for j in range(2**n):
            if bin(j)[2:].zfill(n) not in listt:
                return bin(j)[2:].zfill(n)
                