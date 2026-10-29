
# Method 1
class Solutions:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = set()
        for i in range(len(nums)):
            second =  target - nums[i]
            #print(second)
            if second in seen:
                return [i,nums.index(second)] # this is expensive. Hence go to Method 2
                break
            seen.add(nums[i])

# Method 2
class Solutions_dict:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            second =  target - nums[i]
            #print(second)
            if second in seen:
                return [i,seen[second]]
                break
            seen[nums[i]] = i

if __name__== "__main__":
    a = Solutions()
    b = Solutions_dict()
    nums = [3,2,4]
    print(a.twoSum(nums, 6))
    print(b.twoSum(nums, 6))

