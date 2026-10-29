nums = [0,1,0,3,12]
#expected_output = [1,3,12,0,0]

class Solution:
    def moveZeroes(self,nums:list[int])-> list[int]:
        left = 0
        for right  in range(len(nums)):
            if nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
                left +=1

        return nums


if __name__ == "__main__":
    a = Solution()
    nums = [0, 1, 0, 3, 12]
    print(a.moveZeroes(nums))
