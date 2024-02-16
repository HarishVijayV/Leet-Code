class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dictt=defaultdict(int)
        for i in arr:
            dictt[i]+=1
        listt=[]
        for i,j in dictt.items():
            listt.append([i,j])
        listt=sorted(listt ,key=lambda x:x[1])
        for _ in range(k):
            listt[0][1]-=1
            if listt[0][1]==0:
                listt.pop(0)
        return len(listt)
