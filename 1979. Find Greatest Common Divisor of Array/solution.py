class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        a=nums[0]
        b=nums[len(nums)-1]
        while(True):
            if(a==b):
                return a
            
            if(a<b):
                b=b-a
            
            if(b<a):
                a=a-b
            
        