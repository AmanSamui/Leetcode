class Solution:
    def findLucky(self, arr):
        freq = {}

        # Count frequency
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Find largest lucky integer
        ans = -1

        for key in freq:
            if key == freq[key]:
                ans = max(ans, key)

        return ans
arr = [1,2,2,3,3,3]
obj=Solution()
a=obj.findLucky(arr)

print(a)
