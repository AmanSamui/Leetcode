class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxi=0
        i=0
        n=len(s)
        # Window=set()
        count=0
        for j in range(0,k):
            if s[j] in "aeiou":
                count+=1
            maxi=max(maxi,count)
        j=k
        while j<n:
            if s[j] in "aeiou":
                count+=1
            if s[i] in "aeiou":
                count-=1
            maxi=max(maxi,count)
            i+=1
            j+=1
        return maxi

obj=Solution()
s = "abciiidef"
k = 3
# s = "leetcode"
# k = 3   
# s = "aeiou"
# k = 2
print(obj.maxVowels(s,k))