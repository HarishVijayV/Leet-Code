class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dictt={}
        res=[]
        for i in range(len(groupSizes)):
            if groupSizes[i] not in dictt:
                dictt[groupSizes[i]]=[i]
            else:
                dictt[groupSizes[i]].append(i)
        print(dictt)
        for i,j in dictt.items():
            n=len(j)
            for k in range(0,n,i):
                res.append(j[k:k+i])
        return res

