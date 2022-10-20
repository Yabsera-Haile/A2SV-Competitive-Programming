class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            if task in counts:
                counts[task] += 1
            else:
                counts[task] = 1
        maximum = max(counts.values())
        result = (maximum-1)*(n+1)
        for count in counts.values():
            if count == maximum:
                result += 1
        return max(result, len(tasks))
