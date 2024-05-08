class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans=[]
        cpy=score[:]
        cpy.sort()
        print(cpy)
        for i in score:
            if i==cpy[-1]:
                ans.append("Gold Medal")
            elif i==cpy[-2]:
                ans.append("Silver Medal")
            elif i== cpy[-3]:
                ans.append("Bronze Medal")
            else:
                a=len(cpy)-cpy.index(i)
                ans.append(str(a))
        return ans

        