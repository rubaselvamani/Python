class Solution:
    def reverseWords(self,s: str) -> str:
        lst =  s.split(" ")
        left = 0
        right = len(lst) -1
        while left < right:
            if left < right and lst[left] == '':
                left +=1

            elif left < right and lst[right] == '':
                right -=1

            elif left < right:
                lst[left],lst[right] = lst[right],lst[left]
                left += 1
                right -= 1
        return ' '.join(lst)

if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("I am a cat"))
