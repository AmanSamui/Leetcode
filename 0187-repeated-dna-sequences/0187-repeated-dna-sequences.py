# from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) ->List[str]:
        # print("File is running")
        seen=set()
        result=set()
        n=len(s)
        for i in range(n-9):
            # print("i:",i)
            sequence=s[i:i+10]
            if sequence in seen:
                result.add(sequence)
            seen.add(sequence)      
        return list(result)

obj=Solution()
s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# s = "AAAAAAAAAAAAA"
print(obj.findRepeatedDnaSequences(s))