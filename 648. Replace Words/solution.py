class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        lis=[]
        a=''
        for i in sentence.split(' '):
            root = i
            for j in range(len(i)+1,-1,-1):
                if i[:j] in dictionary:
                    root=i[:j]
            lis.append(root)
        return ' '.join(lis)
            
        