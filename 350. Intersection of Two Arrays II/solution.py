class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans=[]
        for i in nums1:
            if i in nums2:
                ans.append(i)
                nums2.remove(i)
        return ans