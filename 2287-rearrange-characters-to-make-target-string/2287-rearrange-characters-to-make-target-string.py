class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        a=Counter(s)
        b=Counter(target)
        minn=float('inf')
        for i in target:
            if i in b:
                minn=min(minn,a[i]//b[i])
            else:
                return 0
        return minn 

            

        