import  math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1+str2 != str2+str1:
            return ""
        size=math.gcd(len(str1),len(str2))

        return str1[:size]


obj=Solution()
# str1 = "ABCABC"
# str2 = "ABC"

str1 = "ABABAB"
str2 = "ABAB"

print(obj.gcdOfStrings(str1,str2))