class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lis=list(s)
        j=len(lis)-1
        for i in range(len(lis)):
            if i>=j:
                break
            if lis[i].isalpha():
                while not lis[j].isalpha():
                    j-=1
                lis[i],lis[j]=lis[j],lis[i]
                j-=1

        return ''.join(lis)
        
        