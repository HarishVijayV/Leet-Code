class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sor=sorted(arr)
        s=0
        ss=0
        c=0
        for i in  range(len(arr)):
            ss+=sor[i]
            s+=arr[i]
            if ss==s:
                c+=1
        return c
        