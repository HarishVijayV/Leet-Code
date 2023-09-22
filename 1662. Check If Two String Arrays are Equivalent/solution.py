class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for i in range(1,len(word1)):
            word1[0]+=word1[i]
            
        for i in range(1,len(word2)):
            word2[0]+=word2[i]

        if(word1[0]==word2[0]):
            return True 
        else:
            return False