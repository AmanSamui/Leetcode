class Solution(object):
    def isPalindrome(self, s):
        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        return cleaned == cleaned[::-1]
# s = "A man, a plan, a canal: Panama"
s = "race a car"

obj=Solution()

print(obj.isPalindrome(s))