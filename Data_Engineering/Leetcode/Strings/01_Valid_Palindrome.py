class Solution:
    def valid_palindrome(self, s:str)-> bool:
        s = s.lower()
        left = 0
        right = len(s)-1
        while left <right:
            while left < right and not s[left].isalnum():
                left +=1

            while left < right and not s[right].isalnum():
                right -=1

            if s[left] != s[right]:
                return False

            left +=1
            right -=1
        return True





if __name__ == "__main__":
     solution = Solution()
     s = input("enter a string: ")
     print(solution.valid_palindrome(s))



