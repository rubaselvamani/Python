'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        right  = 0
        for right in range(len(t)):
            if len(s) > 0 and len(t) > 0 and s[left] == t[right] :
                left +=1
                if left == len(s):
                    return True
        return False


if __name__ == "__main__":
    is_subsequence = Solution()
    print(is_subsequence.isSubsequence('axc','aebdc'))
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        if len(s) <= 0:
            return True
        else:
            for right in range(len(t)):
                if s[left] == t[right]:
                    left +=1
                    if left == len(s):
                        return True
        return False


if __name__ == "__main__":
    is_subsequence = Solution()
    print(is_subsequence.isSubsequence('',''))
