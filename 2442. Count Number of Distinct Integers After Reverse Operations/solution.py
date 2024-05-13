class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n= len(nums)
        numss=[]
        for i in range(n):
            numss.append(int(str(nums[i])[::-1]))
        return len(set(nums+numss))


        