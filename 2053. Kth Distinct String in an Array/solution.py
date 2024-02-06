class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dictt=defaultdict(int)
        for i in arr:
            dictt[i]+=1
        listt=[]
        for i,j in dictt.items():
            if j==1 :
                listt.append(i)
        try:
            if listt[k-1]:
                return listt[k-1]
        except:
            return ""
