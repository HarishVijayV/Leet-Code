class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dictt={}
        for i in range(len(names)):
            dictt[heights[i]]=names[i]
        heights.sort()
        listt=[]
        for i in range(len(heights)-1,-1,-1):
            listt.append(dictt[heights[i]])
        return listt