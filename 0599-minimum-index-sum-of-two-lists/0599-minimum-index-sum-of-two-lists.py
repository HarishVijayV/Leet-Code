class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minn=3000
        ans=[]
        res=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j] and i+j<=minn:
                    minn=i+j
                    res.append([i,j])
                    print(res)
        for i in res:
            if i[0]+i[1]==minn:
                ans.append(list1[i[0]])
        return ans
        

        
                    
        