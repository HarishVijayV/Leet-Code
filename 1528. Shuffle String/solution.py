class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic={}
        ss=''
        for i,j in zip(indices,s):
            dic[i]=j
        for i in range(len(indices)):
            ss+=dic[i]
        return ss