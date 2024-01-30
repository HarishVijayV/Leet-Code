class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dictt=defaultdict(int)
        c=0
        for i in range(lowLimit,highLimit+1,1):
            for j in str(i):
                c+=int(j)
            dictt[c]+=1
            c=0
        return max(dictt.values())

            

        