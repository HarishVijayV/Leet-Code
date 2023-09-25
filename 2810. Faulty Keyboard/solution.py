class Solution:
    def reverse(self,s:str)->str:
        ss=''
        for i in s:
            ss=i+ss
        return ss
        
    def finalString(self, s: str) -> str:
        sttr=''
        for ch in s:
            if ch=='i':
                sttr =self.reverse(sttr)
            else:
                sttr+=ch
        return sttr
 

