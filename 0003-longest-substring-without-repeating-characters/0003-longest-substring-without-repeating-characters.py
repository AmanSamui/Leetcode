class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(str(s))
        my_dict={}
        left=0
        right=0
        maxi=0
        while right<n:
            if s[right] in my_dict:
                left=max(left,my_dict[s[right]]+1)   # Make valid window
            maxi=max(maxi,right-left+1)    # Updating the maxi value each time if required
            my_dict[s[right]]=right   # storing key along with its current index
            right+=1    # every time incresing window by doing this
        return maxi

        
# s = "abcabcbb"
# s = "bbbbb"
s="pwwkew"

obj=Solution()
print(obj.lengthOfLongestSubstring(s))
            