
class Solution:
    def containsDuplicate(self,nums:list[int])->bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
                break # it is not needed for return but print
            seen.add(num)
        #else: # it is not needed for return but print
        return False

if __name__ == "__main__":
    a = Solution()
    nums = [1, 2, 3, 0]
    print(a.containsDuplicate(nums))
