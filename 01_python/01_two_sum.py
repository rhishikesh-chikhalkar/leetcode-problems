# pylint: disable=invalid-name
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []


def run_test(nums: List[int], target: int) -> None:
    result = Solution().two_sum(nums, target)
    print(f"nums={nums} target={target} --> result={result}")


if __name__ == "__main__":
    run_test([2, 7, 11, 15], 9)
    run_test([3, 2, 4], 6)
    run_test([3, 3], 6)
