class Solution:
    def bac(self,p:str) -> list:
        stack=[]
        for i in p:
            if i!='#':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
        return stack
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.bac(s)==self.bac(t)
        

        