class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = collections.Counter(tasks)
        maximum = max(frequency.values())
        result = (maximum-1)*(n+1)
        for count in frequency.values():
            if count == maximum:
                result += 1
        return max(result, len(tasks))
