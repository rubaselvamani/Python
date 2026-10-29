'''
## in efficient method
nums4 = [1, 3, 5, 7]
nums5 = [2, 4, 6, 8]

nums6 = nums4+nums5
print(nums6)

print(sorted(nums6))
print(nums6.sort())
'''

###### Three pointers algorithm ######

class Solution:
    def merge(self,nums1:list[int],nums2:list[int],m:int,n:int)-> None:
        p1 = m - 1
        p2 = n - 1
        p = (m + n) - 1
        while p2 >= 0:
            if p1>=0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -=1

            else:
                nums1[p] = nums2[p2]
                p2 -=1

            p -=1
        return(nums1)

if __name__ == "__main__":
    nums1 = [2,0]
    nums2 = [1]
    m = 1
    n = 1
    a = Solution()
    print(a.merge(nums1,nums2,m,n))










