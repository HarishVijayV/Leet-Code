class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count=0
        arr=[0,0]
        for i in students:
            arr[i]+=1
        for j in sandwiches:
            if arr[j]==0:
                break
            arr[j]-=1
        return sum(arr)
        