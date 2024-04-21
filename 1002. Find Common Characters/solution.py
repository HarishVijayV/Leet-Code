class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans=[]
        for i in words[0]:
            flag=True
            for k,j in enumerate(words):
                if i not in j:
                    flag=False
                    break
                else:
                    words[k]=j.replace(i,'',1)
            if flag:
                ans.append(i)
        return ans