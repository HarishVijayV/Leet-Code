class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        listt=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j]==nums1[i]:
                    for k in range(j+1,len(nums2),1):
                        if nums2[k]>nums1[i]:
                            listt.append(nums2[k])
                            break
                    if len(listt)<i+1:
                        listt.append(-1)
        return listt




        