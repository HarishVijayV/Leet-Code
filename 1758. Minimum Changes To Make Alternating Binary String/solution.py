class Solution:
    def minOperations(self, s: str) -> int:
        count0=0
        count1=0
        for i,j in enumerate(s):
            if i%2==0:
                if j!='0':
                    count0+=1
                if j!='1':
                    count1+=1
            else:
                if j!="1":
                    count0+=1
                if j!="0":
                    count1+=1
        return min(count1,count0)