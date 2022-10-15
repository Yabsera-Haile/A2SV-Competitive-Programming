class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        result = sorted(map(int, nums), reverse=True)
        return str(result[k-1])
