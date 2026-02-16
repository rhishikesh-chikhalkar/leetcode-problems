class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0

        for i, char in enumerate(s):
            current = values[char]
            next_value = values[s[i + 1]] if i + 1 < len(s) else 0

            if current < next_value:
                total -= current
            else:
                total += current

        return total


def run_test(s: str) -> None:
    result = Solution().romanToInt(s)
    print(f"s={s} -> {result}")


if __name__ == "__main__":
    run_test("III")
    run_test("LVIII")
    run_test("MCMXCIV")
