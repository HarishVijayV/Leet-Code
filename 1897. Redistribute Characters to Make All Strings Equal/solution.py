class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dictt=defaultdict(int)
        for i in words:
            for j in i:
                dictt[j]+=1
        k=dictt[words[0][0]]
        for i in dictt.values():
            if i%len(words)!=0:
                return False
        return True

        