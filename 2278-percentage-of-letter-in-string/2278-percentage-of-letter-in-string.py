class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c=0
        for i in s:
            if i==letter:
                c+=1
        return floor(c/len(s)*100)
        