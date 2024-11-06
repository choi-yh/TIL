class Solution:
    def reverse(self, x: int) -> int:
        result = 0

        is_negative = False
        if x < 0:
            is_negative = True
            x *= -1

        while x:
            result = result * 10 + x % 10
            x //= 10

        if result > 2 ** 31 - 1:
            return 0

        if is_negative:
            result *= -1

        return result
            