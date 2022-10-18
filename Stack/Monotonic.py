class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_index = {num: i for i, num in enumerate(nums1)}
        stack = []
        great_element = [-1] * len(nums1)
        for num in nums2:
            if stack and num > stack[-1]:
                while(stack and num > stack[-1]):
                    great_element[num_index[stack[-1]]] = num
                    stack.pop()
            if num in nums1:
                stack.append(num)
        return great_element