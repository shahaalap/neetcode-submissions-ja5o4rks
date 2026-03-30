class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number, n , result = 0 , len(digits) - 1, []

        for i, num in enumerate(digits):
            number += num * (10 ** (n - i))

        number += 1

        while number > 0:
            x = number % 10
            number = number // 10

            result.append(x)

        result.reverse()
        return result