class Solution:
    def is_subsequence(self,tgt_str:str,sub_str: str)-> bool:
        i= 0
        for char in tgt_str:
            if i <= len(sub_str) and char == sub_str[i]:
                i +=1

        return i == len(sub_str)


if __name__ == "__main__":

    solution = Solution()
    print(solution.is_subsequence("abcde","ace"))
