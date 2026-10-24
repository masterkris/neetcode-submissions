class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        num_times = len(nums) // 3

        elem_map = {}

        for num in nums:
            elem_map[num] = 1 + elem_map.get(num, 0)
        
        res = []

        for val in elem_map:
            if elem_map[val] > num_times:
                res.append(val)
        
        return res


        