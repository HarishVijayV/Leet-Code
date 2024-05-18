class Solution:
    def partitionString(self, s: str) -> int:
        listt=[]
        inter=''
        for i in s:
            if i not in inter:
                inter+=i
            else:
                listt.append(inter)
                inter=i
        listt.append(inter)
        return(len(listt))
        