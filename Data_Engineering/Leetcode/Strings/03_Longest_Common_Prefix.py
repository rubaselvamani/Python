class Solution:
    def longest_common_prefix(self,strs: list[str]) -> str :
        if strs == "":
            return ""
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

            if prefix == "":
                return ""

        return prefix

if __name__ == "__main__":
    sol = Solution()
    print(sol.longest_common_prefix(['flower','flag','fly']))
