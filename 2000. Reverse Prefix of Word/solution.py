class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word:  str
        :type ch: str
        :rtype: str
        """
        s=word
        for i in range(len(word)):
            if word[i]==ch:
                s=(word[:i+1])
                s=s[::-1]
                s+=word[i+1:]
                break
        return s


        