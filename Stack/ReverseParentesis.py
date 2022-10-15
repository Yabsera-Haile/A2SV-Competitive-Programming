class Solution:
    def reverseParentheses(self, s: str) -> str:
        result = []
        for letter in s:
            if (letter == ")"):
                result = "".join(result)
                num = result.rfind("(")
                result = list(result)
                result.pop(num)
                result[num:] = reversed(result[num:])
            else:
                result.append(letter)
        return "".join(result)
