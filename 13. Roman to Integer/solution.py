class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        rom={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev=0
        result=0
        for char in reversed(s):
            current=rom[char]# in each iteration current will have the current iterating letter.
            if(current<prev):
                result=result-current
            else:
                result=result+current
            
            prev=current
        return result

