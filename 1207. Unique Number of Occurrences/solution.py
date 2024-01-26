class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictt=defaultdict(int)
        for i in arr:
            dictt[i]+=1
        return len(dictt.values())==len(set(dictt.values()))
        