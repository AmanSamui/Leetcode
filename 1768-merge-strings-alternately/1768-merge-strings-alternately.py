class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        A,B=len(word1),len(word2)

        i,j=0,0

        s=[]

        word=1

        while i<A and j<B:
            if word==1:
                s.append(word1[i])
                i+=1
                word=2
            else:
                s.append(word2[j])
                j+=1
                word=1
        while i<A:
            s.append(word1[i])
            i+=1
        while j<B:
            s.append(word2[j])
            j+=1
        return ''.join(s)

obj=Solution()
# word1 = "abc"

# word2 = "pqr"

# word1 = "ab"

# word2 = "pqrs"

word1 = "abcd"

word2 = "pq"

print(obj.mergeAlternately(word1,word2))