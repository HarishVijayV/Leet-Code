class Solution:
    def getLucky(self, s: str, k: int) -> int:
        lis=[]
        sum=0
        for i in s:
            lis.extend(list(str(ord(i) - ord('a') + 1)))
        print(lis)
        for _ in range(k):
            sum=0
            for j in lis:
                sum+=int(j)
            lis=list(str(sum))
        return int(''.join(lis))