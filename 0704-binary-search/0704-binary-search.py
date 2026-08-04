class Solution(object):
    def search(self, nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            # print(left,right)
            mid=(left+right)//2 # Basically a index
            # print("mid :",mid)
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target): #Go to right half
                left=mid+1
            else:
                right=mid-1
        return -1

# nums = [2, 3, 4, 5, 3]
# target = 3
# nums = [2, -4, 4, 0, 10]
# target = 6
# nums = [-1,0,3,5,9,12]
# target = 9
nums = [-1,0,3,5,9,12]
target = 2

obj=Solution()
print(obj.search(nums,target))   