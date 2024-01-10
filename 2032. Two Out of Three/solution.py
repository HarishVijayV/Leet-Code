class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        dictt=defaultdict(int)
        listt=[]
        for i in set(nums1):
            dictt[i]+=1
        for i in set(nums2):
            dictt[i]+=1
        for i in set(nums3):
            dictt[i]+=1
        for i,j in dictt.items():
            if j>=2:
                listt.append(i)
        return listt