class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1]*len(nums1)
        dict = {}
        m_stack = []
        for i in range(len(nums1)):
            dict[nums1[i]] = i
        for num2 in nums2:
            if num2 in dict:
                while m_stack and m_stack[-1] < num2:
                    new = m_stack.pop()
                    result[dict[new]] = num2
                m_stack.append(num2)
            else:
                while m_stack and m_stack[-1] < num2:
                    new = m_stack.pop()
                    result[dict[new]] = num2
        return result
