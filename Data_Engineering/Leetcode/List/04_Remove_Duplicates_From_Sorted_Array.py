'''
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output:
'''

class Solution:
    def removeDuplicates(self,nums:list[int])-> list[int]:

        left = 0

        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]

        print(left + 1, nums)

if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    a =Solution()

    print(a.removeDuplicates(nums))




