# from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) ->List[str]:
        # print("File is running")
        seen=dict()
        result=set()
        i=0
        n=len(s)
        while i<n-9:
            # print("i:",i)
            sequence=s[i:i+10]
            if sequence in seen:
                result.add(sequence)
            else:
                seen[sequence]=seen.get(sequence,0)+1   
            i+=1
        return list(result)

obj=Solution()
# s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s = "AAAAAAAAAAAAA"
print(obj.findRepeatedDnaSequences(s))