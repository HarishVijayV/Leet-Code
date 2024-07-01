class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        lis=[]
        for i in word:
            lis.append(ord(i))
        print(lis)
        lis=list(set(lis))
        for i in lis:
            if (i)<91:
                if (i)+32 in lis:
                    c+=1
        return c