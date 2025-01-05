class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dictt=defaultdict(int)
        count=0
        lis1=[]
        lis2=[]
        dic=defaultdict(int)
        for i in words1:
            dictt[i]+=1
        for i in words2:
            dic[i]+=1
        for i, j in dictt.items():
            if j==1:
                lis1.append(i)
        for i, j in dic.items():
            if j==1:
                lis2.append(i)  
        for i in lis1:
            if i in lis2:
                count+=1          
        return count
        