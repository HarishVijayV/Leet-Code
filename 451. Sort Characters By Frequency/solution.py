class Solution:
    def frequencySort(self, s: str) -> str:
        dictt=defaultdict(int)
        str=''
        for i in s:
            dictt[i]+=1
        dictt=dict(sorted(dictt.items() ,key=lambda item:item[1],reverse = True))
        for i,j in dictt.items():
            for _ in range(j):
                str+=i
        return str