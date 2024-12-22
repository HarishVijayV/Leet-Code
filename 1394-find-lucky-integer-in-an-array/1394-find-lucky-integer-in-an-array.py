class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dictt=defaultdict(int)
        lis=[-1]
        for i in arr:
            dictt[i]+=1
        for i, j in dictt.items():
            if i==j:
                lis.append(i)
        return max(lis)

        