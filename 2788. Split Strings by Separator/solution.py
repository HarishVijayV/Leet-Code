class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result=[]
        for i in words:
            result += [w for w in i.split(separator) if w]
        return result