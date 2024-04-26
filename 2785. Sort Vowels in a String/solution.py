class Solution:
    def sortVowels(self, s: str) -> str:
        t=[0]*len(s)
        temp=[]
        for i in range(len(s)):
            if s[i] not in ['a','e','i','o','u','A','E','I','O','U']:
                t[i]=s[i]
            else:
                temp.append(s[i])
        temp.sort()
        k=0
        for i in range(len(t)):
            if t[i]==0:
                t[i]=temp[k]
                k+=1
        return ''.join(t)
