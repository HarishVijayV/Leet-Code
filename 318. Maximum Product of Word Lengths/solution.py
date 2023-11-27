class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def not_in(a,b):
            for i in  a:
                if i in b:
                    return False
            return True
        prod=0
        for i in range(len(words)):
            for j in range(i+1,len(words),1):
                if not_in(words[i],words[j]):
                    prod= max(len(words[i])*len(words[j]),prod)
        return prod