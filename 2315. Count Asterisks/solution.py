class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        c=0
        for i in range(len(s)):
            if s[i]=="|":
                count+=1
            if count%2==0 and s[i]=="*":
                c+=1
        return c


