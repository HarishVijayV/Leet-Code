class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1=num1.split('+')
        num2=num2.split('+')
        a=num1[0]
        aa=num2[0]
        b=num1[1][:-1]
        bb=num2[1]
  
        one=int(a)*int(aa)
        two=int(a)*int(bb[:-1])#i
        three=int(b)*int(aa)#i
        four=int(b)*int(bb[:-1])*(-1)
        ans1=str(one + four)
        tth=str(two+three)
        return ans1+'+'+tth+"i"