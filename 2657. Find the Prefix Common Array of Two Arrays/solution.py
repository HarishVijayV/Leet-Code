class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c=[]
        for i in range(len(A)):
            count=0
            for k in A[0:i+1]:
                if k in B[0:i+1]:
                    count+=1
            c.append(count)
        return c

        