class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count1=0
        count2=0
        n=len(s)/2
        a=s[:n]
        b=s[n:]
        for i in a:
            if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                count1+=1
        for j in b:
            if j in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                count2+=1
        if count1==count2:
            return True
        else:
            return False


        