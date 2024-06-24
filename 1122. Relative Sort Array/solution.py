class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans=[]
        for i in arr2:
            while i in arr1:
                ans.append(i)
                arr1.remove(i)
        arr1.sort()
        ans.extend(arr1)
        return ans