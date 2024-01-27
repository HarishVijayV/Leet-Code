class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        ss=""
        for i in words:
            ss+=i[0]
        if ss==s:
            return True
        else:
            return False
        