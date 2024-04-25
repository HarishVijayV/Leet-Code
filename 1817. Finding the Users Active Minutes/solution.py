class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dictt={}
        for i in logs:
            if i[0] not in dictt:
                dictt[i[0]]=[i[1]]
            elif i[1] not in dictt[i[0]]:
                dictt[i[0]].append(i[1])
        ans=[0]*k
        print(dictt)
        for i,j in dictt.items():
            ans[len(j)-1]+=1
        return ans
            
            