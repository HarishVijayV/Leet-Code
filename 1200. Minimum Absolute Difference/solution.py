class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        listt=[]
        a=abs(arr[1]-arr[0])
        for i in range(len(arr)-1):
            if abs(arr[i+1]-arr[i])<a:
                a=abs(arr[i+1]-arr[i])
        for i in range(len(arr)-1):
            if abs(arr[i+1]-arr[i])==a:
                listt.append([arr[i],arr[i+1]])
        return listt
            
        