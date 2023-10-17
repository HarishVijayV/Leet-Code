class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        c=-1
        if len(arr)<3:
            return False

        for i in range(1,len(arr) - 1):
            if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
                c = i
                break
        if c==-1:
            return False
        i = 0
        while i < c:
            if arr[i] < arr[i + 1]:
                i += 1
                continue
            else:
                return False
        j = c + 1
        while j < len(arr) - 1:
            if arr[j] > arr[j + 1]:
                j += 1
                print(arr[j])
                continue
            else:
                return False
        return True