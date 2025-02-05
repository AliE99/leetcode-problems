class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        result = ""
        for key, value in reversed(symbol.items()):
            quotient = int(num / value)
            result += f"{quotient*key}"
            num = num % value

        return result


num = 3749
print(Solution().intToRoman(num=num))
