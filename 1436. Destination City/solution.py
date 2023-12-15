class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        listt=[]
        dictt=defaultdict(int)
        for i in paths:
            dictt[i[0]]+=1
            dictt[i[1]]-=1
        for i,j in dictt.items():
            if j==-1:
                return i
