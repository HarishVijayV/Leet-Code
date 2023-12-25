class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        strr=""
        count=0
        for i in s.split(" "):
            strr=strr+i+" "
            count+=1
            if count==k:
                break
        return strr[:-1]