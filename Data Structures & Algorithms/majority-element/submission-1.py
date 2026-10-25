class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        elem_map = {}
        majority_num = len(nums) // 2

        for num in nums:
            elem_map[num] = 1 + elem_map.get(num, 0)
            if elem_map[num] > majority_num:
                return num
        
        return -1
                