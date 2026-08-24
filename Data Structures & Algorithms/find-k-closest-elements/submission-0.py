class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if k == len(arr):
            return arr

        l = 0
        res = []

        for r in range(len(arr)):
            res.append(arr[r])

            # res[0] smallest val.
            # res[-1] largest val.

            while len(res) > k:
                if abs(res[0] - x) > abs(res[len(res) - 1] - x):
                    res.pop(0)
                    l += 1
                else:
                    res.pop()

        return res




        