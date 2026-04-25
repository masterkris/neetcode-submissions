class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # l, r pointers
        # 1, len(numbers) - 1-indexed
        # [1,2,3,4], target = 3
        # 1 + 4 = 5, too large --> move r pointer left by 1
        # else do opposite
        # return

        l, r = 0, len(numbers)-1

        while l < r:
            compare = numbers[l] + numbers[r]

            if compare > target:
                r -= 1
            elif compare < target:
                l += 1
            else:
               return [l+1, r+1] # 1-indexed