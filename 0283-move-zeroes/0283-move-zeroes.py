class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        temp=[]
        j=0
        for i in range(0,n):
            if(nums[i]!=0):
                temp.append(nums[i])
                j+=1
        for _ in range(0,n-j):
            temp.append(0)
        nums[:]=temp
        return nums

# nums = [0, 1, 4, 0, 5, 2]
# nums=[0, 0, 0, 1, 3, -2]
nums = [0,1,0,3,12]
obj=Solution()
print(obj.moveZeroes(nums))
