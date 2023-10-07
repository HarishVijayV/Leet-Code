class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s=list(s)
        for i in range(len(s)):
            if (ord(s[i])>=ord("a") and ord(s[i])<=ord('z')) or ((s[i])>='0' and (s[i]) <='9'):
                continue
            else:
                s[i]=''
        s=''.join(s)
        if s==s[::-1]:
            return True
        else:
            return False
            