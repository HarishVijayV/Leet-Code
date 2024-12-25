class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        dict1=defaultdict(int)
        dict2=defaultdict(int)
        for i in word1:
            dict1[i]+=1
        for i in word2:
            dict2[i]+=1
        for i in (word1):
            if abs(dict1[i]-dict2[i])>3:
                return False
        for i in (word2):
            if abs(dict1[i]-dict2[i])>3:
                return False
        return True

        