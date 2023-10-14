class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        ans=[]
        nums=[]
        k=0
        for i in range(len(words)):
            if words[i]=="prev":
                k+=1
                if k<=len(nums):
                    nums.reverse()
                    ans.append(int(nums[k-1]))
                    nums.reverse()
                else:
                    ans.append(-1)    
            else:
                nums.append(int(words[i]))
                k=0
        return ans