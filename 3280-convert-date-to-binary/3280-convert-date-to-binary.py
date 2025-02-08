class Solution:
    def convertDateToBinary(self, date: str) -> str:
        def bina(x):
            lis=[]
            while x>0:
                lis.append(str(mod(x,2)))
                x=x//2
            return ''.join(lis[::-1])
        a,b,c= date.split('-')

        return bina(int(a))+'-'+bina(int(b))+'-'+bina(int(c))