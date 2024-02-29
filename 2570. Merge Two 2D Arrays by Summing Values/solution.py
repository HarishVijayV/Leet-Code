class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dictt=defaultdict(int)
        listt=[]
        for i in range(len(nums1)):
            dictt[nums1[i][0]]+=nums1[i][1]
        for i in range(len(nums2)):
            dictt[nums2[i][0]]+=nums2[i][1]    
        for i,j in dictt.items():
            listt.append([i,j]) 
        listt=sorted(listt,key=lambda x:x[0]) 
        return listt
            
