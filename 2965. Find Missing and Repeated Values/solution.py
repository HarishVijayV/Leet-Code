class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dictt=defaultdict(int)
        ans=[]
        for i in grid:
            for j in i:
                dictt[j]+=1
        for i,j in dictt.items():
            if j==2:
                ans.append(i)
        for i in range(1,len(grid)**2+1):
            if i not in dictt:
                ans.append(i)
        return ans
        
        