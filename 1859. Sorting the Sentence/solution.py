class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        c=''
        a=['']*len(s.split())
        for i in s.split():
            ii=int(i[-1])-1
            a[ii]=i[:-1]+" "
        c=c.join(a)
        return c[:-1]
       