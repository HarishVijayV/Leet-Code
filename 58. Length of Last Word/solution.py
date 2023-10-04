class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        s=s.split()
        a=s[-1]
        for aa in a:
            count+=1
        return count

        