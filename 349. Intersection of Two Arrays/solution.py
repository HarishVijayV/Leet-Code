class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        listt=[]
        for i in nums1:
            if i in nums2:
                listt.append(i)
                nums2.remove(i)
        return list(set(listt))

        