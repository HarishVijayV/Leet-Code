class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dictt=defaultdict(int)
        listt=[]
        for i in s1.split():
            dictt[i] += 1
        for i in s2.split():
            dictt[i] +=1
        for i,j in dictt.items():
            if j==1:
                listt.append(i)
        return listt 