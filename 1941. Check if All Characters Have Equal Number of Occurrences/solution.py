class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dictt=defaultdict(int)
        for i in s:
            dictt[i]+=1
        count=dictt[s[0]]
        for j in dictt.values():
            if j!=count:
                return False
        return True

