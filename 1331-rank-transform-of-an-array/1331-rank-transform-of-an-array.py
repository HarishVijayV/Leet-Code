class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        cop=copy.deepcopy(arr)
        dictt=defaultdict(int)
        ans=[0]*len(arr)
        cop.sort()
        j=0
        for i in range(len(cop)):
            if not dictt[cop[i]]:
                dictt[cop[i]]=j+1
                j+=1
        for i in range(len(arr)):
            ans[i]=dictt[arr[i]]
        return ans

        