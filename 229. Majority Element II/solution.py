class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dictt={}
        peak=len(nums)/3
        for i in nums:
            if i in dictt:
                dictt[i]+=1
            else:
                dictt[i]=1
        result=[k for k,v in dictt.items() if v>peak]
        return result
