class Solution:

    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = set('aeiouAEIOU')
        # two pointer approach
        left_index = 0
        right_index = len(s_list) - 1

        while left_index < right_index:
            if s_list[left_index] not in vowels:
                left_index += 1
            elif s_list[right_index] not in vowels:
                right_index -= 1
            else:
                s_list[left_index], s_list[right_index] = s_list[right_index], s_list[left_index]
                left_index += 1
                right_index -= 1
        return "".join(s_list)

if __name__ == "__main__":
    vr = Solution()
    print(vr.reverseVowels("IceCreAm"))
