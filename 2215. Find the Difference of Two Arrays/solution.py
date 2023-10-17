class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        listt=[[],[]]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                continue
            else:
                listt[0].append(nums1[i]) 
        listt[0]=list(set(listt[0]))
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                continue
            else:
                listt[1].append(nums2[i]) 
        listt[1]=list(set(listt[1]))
        return listt