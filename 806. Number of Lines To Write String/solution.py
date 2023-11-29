class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        count=0
        line=1
        for i in s:
            count+=widths[ord(i)-97]
            if count>100:
                line+=1
                count=widths[ord(i)-97]
        return [line,count]
            