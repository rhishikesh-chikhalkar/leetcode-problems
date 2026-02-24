from typing import List


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


def run_test(strs: List[str]) -> None:
    result = Solution().longest_common_prefix(strs)
    print(f"strs={strs} --> result='{result}'")


if __name__ == "__main__":
    run_test(["flower", "flow", "flight"])
    run_test(["dog", "racecar", "car"])
