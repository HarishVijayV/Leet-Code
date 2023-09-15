class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out=""
        strs.sort()
        a=strs[0]
        b=strs[-1]
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if a[i]==b[i]:
                out+=(a[i])
            else:
                break
        return out

