class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        listt=[]
        count=0
        for i in nums1:
            if i in nums2:
                count+=1
        listt.append(count)
        count=0
        for j in nums2:
            if j in nums1:
                count+=1
        listt.append(count)
        return listt