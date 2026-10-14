class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
    
        n=len(nums)
        nums.sort()
        count=0
        last_smaller=float("-inf")
        longest=0
        for i in range(0,n):
            num=nums[i]
            if num-1==last_smaller:
                count+=1
                last_smaller=num
            elif num != last_smaller:
                count=1
                last_smaller=num
            longest=max(longest,count)
        return longest

nums=[1,99,101,98,2,5,3,100,1,1]

result=Solution()
print(result.longestConsecutive(nums))