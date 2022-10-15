class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        dict = {3 : "Fizz", 5 : "Buzz"}
        for i in range(1, n + 1):
            arr = []
            for key in [3,5]:
                if i % key == 0:
                    arr.append(dict[key])
            if not arr:
                arr.append(str(i))
            result.append(''.join(arr))
        return result
# print(Solution().fizzBuzz(n=15))
