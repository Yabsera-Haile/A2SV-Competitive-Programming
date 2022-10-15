class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = []
        nums.sort()
        start = 0
        end = len(nums)-1
        while start <= end:
            result.append(nums[start])
            start += 1
            if start < end:
                result.append(nums[end])
                end -= 1
        return result
