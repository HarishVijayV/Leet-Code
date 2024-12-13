class Solution:
    def findScore(self, nums: List[int]) -> int:
        a=sorted(nums)
        score=0
        used=[False]*len(a)

        for num in a:
            for i in range(len(nums)):
                if nums[i]==num and not used[i]:
                    score+=num
                    used[i]=True
                    if i>0 and not used[i-1]:
                        used[i-1]=True
                    if i<len(nums)-1 and not used[i+1]:
                        used[i+1]=True
                    break
        return score

                
