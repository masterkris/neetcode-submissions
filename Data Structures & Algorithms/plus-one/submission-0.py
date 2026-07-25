class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # Case 1: (less than 9)
        # add 1 to last digit if less than 9
        # return

        # Case 2: (not less than 9)
        # iterate and make digit 0


        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + digits # all digits were 9 if loop ends
        