class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max=0
        for i in sentences:
            count=0
            for j in i.split():
                count+=1
            if count> max:
                max=count
        return max