from typing import List


class Solution:
    def is_valid(self, s: str) -> bool:
        """Return True if every bracket in s is closed in the correct order."""
        stack: List[str] = []
        closing_to_opening = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in closing_to_opening.values():
                stack.append(char)
                continue

            if not stack or stack[-1] != closing_to_opening.get(char, ""):
                return False

            stack.pop()

        return not stack


def run_test(s: str) -> None:
    result = Solution().is_valid(s)
    print(f"s={s!r} --> result={result}")


if __name__ == "__main__":
    run_test("()")
    run_test("()[]{}")
    run_test("(]")
    run_test("([])")
    run_test("([)]")
