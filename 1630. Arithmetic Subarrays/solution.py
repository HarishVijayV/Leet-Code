class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        sub=[]
        ans=[]
        for i in range(len(l)):
            sub=nums[l[i]:r[i]+1]
            sub.sort()
            a=sub[1]-sub[0]
            for i in range(len(sub)-1):
                print(a)
                if sub[i+1]-sub[i]!=a:
                    ans.append(False)
                    break
                elif len(sub)-2==i:
                    ans.append(True)
        return ans             




        