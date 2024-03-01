class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        dictt=defaultdict(int)
        for i in s:
            dictt[i]+=1
        o_count=dictt['0']
        l_count=dictt['1']
        print(l_count)
        ans=''
        if l_count>1:
            for i in range(l_count-1):
                ans+='1'
            for i in range(o_count):
                ans+='0'
            ans+='1'
        else:
            for i in range(o_count):
                ans+='0'
            ans+='1'
        return ans   
        