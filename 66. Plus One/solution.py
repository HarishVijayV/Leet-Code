class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a="".join(map(str,digits))
        b=int(a)+1
        b=list(str(b))
        b=list(map(int,b))
        return b
    