class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i]-nums[j])>=valueDifference and abs(i - j) >= indexDifference:
                    ans.append(i)
                    ans.append(j)
                    return ans
        ans.append(-1)
        ans.append(-1)
        return ans
                
                    
                    