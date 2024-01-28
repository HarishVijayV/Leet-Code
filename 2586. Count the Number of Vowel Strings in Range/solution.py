class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count=0
        aa=['a','e','i','o','u']
        for i in range(left,right+1):
            if words[i][0] in aa and words[i][-1] in aa:
                count+=1
        return count

        