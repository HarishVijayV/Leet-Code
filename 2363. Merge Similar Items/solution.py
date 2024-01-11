class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dictt=defaultdict(int)
        for i in items1:
            dictt[i[0]]+=i[1]
        for i in items2:
            dictt[i[0]]+=i[1]
        listt=[]
        for i,j in dictt.items():
            listt.append([i,j])
        listt=sorted(listt,key=lambda x:x[0])
        return listt
        