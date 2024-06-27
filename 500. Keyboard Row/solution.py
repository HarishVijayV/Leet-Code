from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiopQWERTYUIOP"
        second = "asdfghjklASDFGHJKL"
        third = "zxcvbnmZXCVBNM"
        ans=[]
        for i in words:
            c=0
            if i[0] in first:
                for j in i:
                    if j not in first:
                        break
                    else:
                        c+=1
                if c==len(i):
                    ans.append(i)   
            if i[0] in second:
                for j in i:
                    if j not in second:
                        break
                    else:
                        c+=1          
                if c==len(i):
                    ans.append(i)                                         
            if i[0] in third:
                for j in i:
                    if j not in third:
                        break
                    else:
                        c+=1
                if c==len(i):
                    ans.append(i)   
        return ans             
                        