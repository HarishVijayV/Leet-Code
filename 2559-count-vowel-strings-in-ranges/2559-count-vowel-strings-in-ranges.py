class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans=[]
        vowelss={'a','e','i','o','u'}
        helpp=[]
        for i in words:
            if i[0] in vowelss and i[-1] in vowelss:
                helpp.append(1)
            else:
                helpp.append(0)

        for i in range(1, len(helpp)):
            helpp[i] += helpp[i - 1]

        for i in queries:
            l=i[0]
            r=i[1]
            if l==0:
                c=helpp[r]
            else:
                c=helpp[r]-helpp[l-1]
            ans.append(c)

        return ans
