class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=[' ']*len(nums)
        i=0
        j=(len(nums)-1)
        for k in nums:
            if k%2!=0:
                arr[j]=k
                j-=1
            else:
                arr[i]=k
                i+=1
        return arr

