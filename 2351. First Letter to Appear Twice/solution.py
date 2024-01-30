class Solution:
    def repeatedCharacter(self, s: str) -> str:
        listt=[]
        for i in  s:
            if i in listt:
                return i
            else:
                listt.append(i)
            
        