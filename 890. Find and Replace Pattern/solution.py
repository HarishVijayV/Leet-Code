class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans=[]
        for i in words:
            if len(set(i))==len(set(pattern))==len(set(zip(i, pattern))):
                ans.append(i)
        return ans
        