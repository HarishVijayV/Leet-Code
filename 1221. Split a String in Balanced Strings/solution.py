class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rc=0
        lc=0
        count=0
        for i in s:
            if i=='R':
                rc+=1
            if i== 'L':
                lc+=1
            if rc==lc:
                count+=1
                rc=0
                lc=0
        return count
        