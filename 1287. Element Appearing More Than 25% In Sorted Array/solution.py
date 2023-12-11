class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        qtr=len(arr)//4
        count=1
        if len(arr)<=2:
            return arr[0]
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                count+=1
                if count>qtr:
                    return int(arr[i])
            else:
                count=1
        return -1


        