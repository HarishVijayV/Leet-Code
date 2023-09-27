class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss=''
        for i in s.split():
            ss=ss+i[::-1]+" "
        return ss[:-1]
        