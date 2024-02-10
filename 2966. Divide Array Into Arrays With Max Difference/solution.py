class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        listt=[]
        for i in range(0,len(nums)-2,3):
            if not abs(nums[i]-nums[i+2])<=k:
                return []
            else:
                listt.append([nums[i],nums[i+1],nums[i+2]])
        return listt