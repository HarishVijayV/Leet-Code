class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        maxx=0
        ans=-1
        s=paragraph.lower()
        s = re.sub(r'[^\w\s]', ' ', s)  # Replace all non-alphanumeric characters with space
        dictt=defaultdict(int)
        for i in s.split():
            if i not in banned:
                dictt[i]+=1
        maxx=max(dictt.values())
        for i , j in dictt.items():
            if j==maxx:
                maxx=j
                ans=i
        return ans

        
